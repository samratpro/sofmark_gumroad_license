import requests
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QFont, QFontDatabase
from PyQt6.QtCore import QThread, pyqtSignal
from ui.license_ui import Ui_Form
from features.license_manage import view_license, create_or_update_license, remove_all_files
from features.data_save_signals import signals
from datetime import datetime, timedelta
from models import Session, Notification

GUMROAD_PRODUCT_ID = "m8P4pqFnq91JmZy0MkE18g=="
access_token = "9BxeJ6xlF-AXcQi0NlC2oZ02ILcz9Z9UfVpZPIrA9BM"
trail_credit = 10
reset_mode = "Daily"  # Weekly, Monthly, Yearly

class LicenseWorker(QThread):
    # Signals for communication with the main thread
    error = pyqtSignal(str)
    success = pyqtSignal(str)
    finished = pyqtSignal()

    def __init__(self, license_key, license_data, access_token, product_id):
        super().__init__()
        self.license_key = license_key
        self.license_data = license_data
        self.access_token = access_token
        self.product_id = product_id

    def run(self):
        try:
            if self.license_data:
                url = "https://api.gumroad.com/v2/licenses/enable"
                payload = {
                    "access_token": self.access_token,
                    "product_id": self.product_id,
                    "license_key": self.license_key
                }
                response = requests.put(url, data=payload)
            else:
                url = "https://api.gumroad.com/v2/licenses/verify"
                payload = {
                    "product_id": self.product_id,
                    "license_key": self.license_key
                }
                response = requests.post(url, data=payload)

            if response.status_code != 200:
                self.error.emit("Gumroad API request failed.")
                return

            gumroad_response = response.json()
            if not gumroad_response.get("success"):
                self.error.emit(gumroad_response.get("message", "Invalid license key."))
                return

            purchase = gumroad_response.get("purchase", {})
            uses = purchase.get("uses", 0)
            price = purchase.get("price", 0)

            if uses > 0:
                self.error.emit("License already in use.")
                return

            if self.license_data and self.license_data.get('price') == 0 and price == 0:
                self.error.emit("You are already using a trial. Another trial not allowed without license removal.")
                return

            plan = "Trial" if price == 0 else "Lifetime"
            create_or_update_license(self.license_key, price, trail_credit if plan == "Trial" else 0, plan, "Never", reset_mode)
            self.success.emit("License successfully updated.")

        except Exception as e:
            self.error.emit(f"Error updating license: {str(e)}")
        finally:
            self.finished.emit()

class licensePage(QWidget):
    def __init__(self, username=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.username = username
        self.session = Session()

        # Setup fonts
        self.setup_fonts()
        # Initialize UI
        self.setup_ui()
        signals.license_saved.connect(self.setup_ui)

    def setup_fonts(self):
        font_bold_id = QFontDatabase.addApplicationFont("font/Inter_18pt-Bold.ttf")
        font_regular_id = QFontDatabase.addApplicationFont("font/OpenSans-Regular.ttf")

        font_bold = QFont(QFontDatabase.applicationFontFamilies(font_bold_id)[0], 13)
        font_regular = QFont(QFontDatabase.applicationFontFamilies(font_regular_id)[0], 11)

        self.apply_font_to_all_widgets(font_regular)
        self.apply_fonts_by_object_names(font_bold, ["label"])

    def apply_font_to_all_widgets(self, font: QFont):
        for widget in self.findChildren(QWidget):
            widget.setFont(font)

    def apply_fonts_by_object_names(self, font: QFont, object_names: list):
        for name in object_names:
            widget = self.findChild(QWidget, name)
            widget.setFont(font)

    def setup_ui(self):
        self.ui.error.setText("")
        self.ui.sucess.setText("")
        data = view_license()

        if data:
            self.ui.license_status.setText("Activated")
            self.ui.exp_date_status.setText(data['expiry'])
            self.ui.last_activate_time.setText(data['activate_time'])
            self.ui.price.setText('$' + str(data.get('price', 0)))
        else:
            self.ui.license_hide_lebel.hide()
            self.ui.remove_license.hide()
            self.ui.license_status.setText("Not Activated")
            self.ui.exp_date_status.setText("N/A")
            self.ui.last_activate_time.setText("N/A")
            self.ui.price.setText('$0')

        self.ui.update_license.clicked.connect(lambda: self.update_license(view_license()))
        self.ui.remove_license.clicked.connect(lambda: self.remove_license(view_license()))

    def update_license(self, license_data):
        LICENSE_KEY = self.ui.license_key.text().strip()
        if not LICENSE_KEY:
            self.ui.error.setText("Please input a valid license key.")
            QtWidgets.QMessageBox.information(None, "Info", "Please input a valid license key.")
            return

        # Show waiting message
        self.ui.error.setText("Please wait...")
        self.ui.update_license.setEnabled(False)  # Disable button to prevent multiple clicks

        # Create and start worker thread
        self.worker = LicenseWorker(LICENSE_KEY, license_data, access_token, GUMROAD_PRODUCT_ID)
        self.worker.error.connect(self.on_error)
        self.worker.success.connect(self.on_success)
        self.worker.finished.connect(self.on_finished)
        self.worker.start()

    def on_error(self, message):
        self.ui.error.setText(message)
        QtWidgets.QMessageBox.information(None, "Info", message)

    def on_success(self, message):
        self.ui.sucess.setText(message)
        self.ui.license_hide_lebel.show()
        self.ui.remove_license.show()
        self.ui.license_key.setText('')
        QtWidgets.QMessageBox.information(None, "Info", message)
        Notification.add_notification(self.session, message)

    def on_finished(self):
        self.ui.error.setText("")
        self.ui.update_license.setEnabled(True)  # Re-enable button

    def remove_license(self, license_data):
        try:
            # Check trial restriction
            last_reset_str = license_data.get('last_reset')
            if last_reset_str:
                try:
                    last_reset = datetime.strptime(last_reset_str, "%Y-%m-%d %H:%M:%S")
                    if license_data.get('price') == 0 and datetime.now() - last_reset < timedelta(hours=0.001):
                        self.ui.error.setText(
                            "Trial license can't be removed within 24 hours. If you have paid license direct update it")
                        QtWidgets.QMessageBox.information(None, "Info",
                                                          "Trial license can't be removed within 24 hours. If you have paid license direct update it")
                        return
                except ValueError:
                    pass  # If last_reset is invalid format, ignore restriction

            # Call Gumroad decrement uses (optional)
            url = "https://api.gumroad.com/v2/licenses/decrement_uses_count"
            payload = {
                "access_token": access_token,
                "product_id": GUMROAD_PRODUCT_ID,
                "license_key": license_data.get("license")
            }
            response = requests.put(url, data=payload)

            if response.status_code == 200:
                gumroad_response = response.json()
                if gumroad_response.get("success", False):
                    remove_all_files()
                    self.ui.license_hide_lebel.hide()
                    self.ui.remove_license.hide()
                    self.ui.sucess.setText("License removed.")
                    QtWidgets.QMessageBox.information(None, "Info","License removed.")
                    Notification.add_notification(self.session, "License removed.")
                else:
                    self.ui.error.setText(f"Failed to remove: {gumroad_response.get('message', 'Unknown error')}")
                    QtWidgets.QMessageBox.information(None, "Info", "Failed to remove")
            else:
                self.ui.error.setText("Gumroad API request failed.")
                QtWidgets.QMessageBox.information(None, "Info", "Gumroad API request failed.")

        except Exception as e:
            pass