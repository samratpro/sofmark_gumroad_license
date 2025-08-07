import logging
import requests
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QWidget, QMessageBox
from PyQt6.QtGui import QFont, QFontDatabase
from ui.license_ui import Ui_Form
from features.license_manage import view_license, create_or_update_license, remove_all_files
from features.data_save_signals import signals
from models import Session, Notification
from datetime import datetime, timedelta

# Configure logger
logging.basicConfig(
    filename="license.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Config constants
GUMROAD_PRODUCT_ID = "m8P4pqFnq91JmZy0MkE18g=="
ACCESS_TOKEN = "9BxeJ6xlF-AXcQi0NlC2oZ02ILcz9Z9UfVpZPIrA9BM"
RESET_MODE = "Daily"
TRIAL_CREDIT = 10

class licensePage(QWidget):
    def __init__(self, username=None):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.username = username
        self.session = Session()

        self.setup_fonts()
        self.setup_ui()
        signals.license_saved.connect(self.setup_ui)

    def setup_fonts(self):
        try:
            font_bold_id = QFontDatabase.addApplicationFont("font/Inter_18pt-Bold.ttf")
            font_regular_id = QFontDatabase.addApplicationFont("font/OpenSans-Regular.ttf")

            font_bold = QFont(QFontDatabase.applicationFontFamilies(font_bold_id)[0], 13)
            font_regular = QFont(QFontDatabase.applicationFontFamilies(font_regular_id)[0], 11)

            self.apply_font_to_all_widgets(font_regular)
            self.apply_fonts_by_object_names(font_bold, ["label"])
        except Exception as e:
            logger.warning(f"Font setup failed: {e}")

    def apply_font_to_all_widgets(self, font):
        for widget in self.findChildren(QWidget):
            widget.setFont(font)

    def apply_fonts_by_object_names(self, font, object_names):
        for name in object_names:
            widget = self.findChild(QWidget, name)
            if widget:
                widget.setFont(font)

    def setup_ui(self):
        self.ui.error.setText("")
        self.ui.sucess.setText("")
        self.ui.license_key.setText("")
        data = view_license()

        if data:
            self.ui.license_status.setText("Activated")
            self.ui.exp_date_status.setText(data.get('expiry', 'N/A'))
            self.ui.last_activate_time.setText(data.get('activate_time', 'N/A'))
            self.ui.price.setText('$' + str(data.get('price', 0)))
            self.ui.license_hide_lebel.show()
            self.ui.remove_license.show()
        else:
            self.ui.license_hide_lebel.hide()
            self.ui.remove_license.hide()
            self.ui.license_status.setText("Not Activated")
            self.ui.exp_date_status.setText("N/A")
            self.ui.last_activate_time.setText("N/A")
            self.ui.price.setText('$0')

        try:
            self.ui.update_license.clicked.disconnect()
        except Exception:
            pass

        try:
            self.ui.remove_license.clicked.disconnect()
        except Exception:
            pass

        self.ui.update_license.clicked.connect(self.update_license)
        self.ui.remove_license.clicked.connect(self.remove_license)

    def update_license(self):
        license_key = self.ui.license_key.text().strip()
        self.ui.error.setText("")
        self.ui.sucess.setText("")

        if not license_key:
            self.show_message("Please input a valid license key.", error=True)
            self.ui.error.setText("Please input a valid license key.")
            return

        self.ui.error.setText("Please wait...")
        self.ui.update_license.setEnabled(False)
        QtWidgets.QApplication.processEvents()

        try:
            existing_data = view_license()
            if existing_data:
                url = "https://api.gumroad.com/v2/licenses/enable"
                payload = {
                    "access_token": ACCESS_TOKEN,
                    "product_id": GUMROAD_PRODUCT_ID,
                    "license_key": license_key
                }
                response = requests.put(url, data=payload)
            else:
                url = "https://api.gumroad.com/v2/licenses/verify"
                payload = {
                    "product_id": GUMROAD_PRODUCT_ID,
                    "license_key": license_key
                }
                response = requests.post(url, data=payload)

            if response.status_code != 200:
                self.ui.error.setText("Invalid License Key")
                return

            gumroad_response = response.json()
            if not gumroad_response.get("success"):
                self.ui.error.setText(gumroad_response.get("message", "Invalid license key."))
                return

            purchase = gumroad_response.get("purchase", {})
            uses = purchase.get("uses", 0)
            price = purchase.get("price", 0)

            if uses > 0:
                self.ui.error.setText("License already in use.")
                return

            if existing_data and existing_data.get('price') == 0 and price == 0:
                self.ui.error.setText("You are already using a trial. Another trial not allowed without license removal.")
                return

            plan = "Trial" if price == 0 else "Lifetime"
            create_or_update_license(license_key, price, TRIAL_CREDIT if plan == "Trial" else 0, plan, "Never", RESET_MODE)
            self.show_success("License successfully updated.")

        except Exception as e:
            self.ui.error.setText(f"Error updating license: {str(e)}")
            logger.exception("Exception occurred during license update.")
        finally:
            self.ui.update_license.setEnabled(True)

    def remove_license(self):
        self.ui.error.setText("")
        self.ui.sucess.setText("")

        license_data = view_license()
        if not license_data:
            self.ui.error.setText("No active license to remove.")
            return

        last_reset_str = license_data.get('last_reset')
        try:
            if last_reset_str:
                last_reset = datetime.strptime(last_reset_str, "%Y-%m-%d %H:%M:%S")
                if license_data.get('price') == 0 and datetime.now() - last_reset < timedelta(hours=0.001):
                    self.ui.error.setText("Trial license can't be removed within 24 hours. If you have paid license, directly update it.")
                    return
        except ValueError:
            pass

        try:
            url = "https://api.gumroad.com/v2/licenses/decrement_uses_count"
            payload = {
                "access_token": ACCESS_TOKEN,
                "product_id": GUMROAD_PRODUCT_ID,
                "license_key": license_data.get("license")
            }
            response = requests.put(url, data=payload)

            if response.status_code == 200:
                gumroad_response = response.json()
                if gumroad_response.get("success", False):
                    remove_all_files()
                    self.ui.sucess.setText("License removed.")
                    Notification.add_notification(self.session, "License removed.")
                    self.setup_ui()
                else:
                    self.ui.error.setText(f"Failed to remove: {gumroad_response.get('message', 'Unknown error')}")
            else:
                self.ui.error.setText("Gumroad API request failed.")

        except Exception as e:
            self.ui.error.setText(f"Error removing license: {str(e)}")
            logger.exception("Exception during license removal")

    def show_message(self, message, error=False):
        title = "Error" if error else "Info"
        QMessageBox.information(self, title, message)
        logger.info(f"Message shown to user: {title} - {message}")

    def show_success(self, message):
        self.ui.sucess.setText(message)
        self.ui.license_key.setText("")
        Notification.add_notification(self.session, message)
        self.setup_ui()
