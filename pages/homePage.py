from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QDesktopServices, QFont, QFontDatabase
from PyQt6.QtCore import QUrl
from ui.home_ui import Ui_Form
from models import Session, Notification
import socket
import uuid
import requests
from datetime import datetime
from features.license_manage import view_license
from features.data_save_signals import signals

LINKEDIN_URL = "https://www.linkedin.com/in/samratpy/"
domain = "http://127.0.0.1:8000"


class homepage(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.session = Session()

        self.setup_fonts()
        self.setup_ui()

    def setup_fonts(self):
        font_bold_id = QFontDatabase.addApplicationFont("font/Inter_18pt-Bold.ttf")
        font_regular_id = QFontDatabase.addApplicationFont("font/OpenSans-Regular.ttf")
        font_light_id = QFontDatabase.addApplicationFont("font/Inter_24pt-Light.ttf")

        font_bold = QFont(QFontDatabase.applicationFontFamilies(font_bold_id)[0], 13)
        font_regular = QFont(QFontDatabase.applicationFontFamilies(font_regular_id)[0], 11)
        font_light = QFont(QFontDatabase.applicationFontFamilies(font_light_id)[0], 10)

        self.apply_font_to_all_widgets(font_regular)
        self.apply_fonts_by_object_names(font_bold, ["explore_leb", "label_10", "label", "credit","label_2","label_3","label_4"])
        self.apply_fonts_by_object_names(font_light, ["reset_time_status"])

    def apply_font_to_all_widgets(self, font: QFont):
        for widget in self.findChildren(QWidget):
            widget.setFont(font)

    def apply_fonts_by_object_names(self, font: QFont, object_names: list):
        for name in object_names:
            widget = self.findChild(QWidget, name)
            if widget:
                widget.setFont(font)

    def setup_ui(self):
        # Notification label mapping
        self.license_data = view_license() or {}
        self.notification_frames = [
            (self.ui.notice_1, self.ui.notice_leb_1, self.ui.notice_time_1),
            (self.ui.notice_2, self.ui.notice_leb_2, self.ui.notice_time_2),
            (self.ui.notice_3, self.ui.notice_leb_3, self.ui.notice_time_3),
            (self.ui.notice_4, self.ui.notice_leb_4, self.ui.notice_time_4),
            (self.ui.notice_5, self.ui.notice_leb_5, self.ui.notice_time_5),
            (self.ui.notice_6, self.ui.notice_leb_6, self.ui.notice_time_6),
            (self.ui.notice_7, self.ui.notice_leb_7, self.ui.notice_time_7),
            (self.ui.notice_8, self.ui.notice_leb_8, self.ui.notice_time_8)
        ]

        # Load initial license info
        self.refresh_license_info()

        # Connect developer links
        self.ui.explore_more.clicked.connect(lambda: self.open_url(LINKEDIN_URL))
        self.ui.contact_developer.clicked.connect(lambda: self.open_url(LINKEDIN_URL))

        # Connect signals
        signals.notification_saved.connect(self.load_notifications)
        signals.credit_saved.connect(self.load_credit)
        signals.license_saved.connect(self.refresh_license_info)

        # Initial load
        self.load_notifications()

    def refresh_license_info(self):
        """Refresh license-related UI when license changes."""
        self.license_data = view_license() or {}

        # Set MAC & IP
        self.mac_address = self.license_data.get('mac', self.get_mac_address())
        self.ip_address = self.license_data.get('ip', self.get_local_ip())
        self.ui.mac.setText(self.mac_address)
        self.ui.ip.setText(self.ip_address)

        # Location
        location = self.license_data.get('location')
        if location:
            self.ui.location.setText(location)
        else:
            self.get_location()

        # License UI
        self.ui.activate_status.setText("Activate" if self.license_data.get('license') else "Not Activate")
        self.ui.license_type_status.setText(self.license_data.get("license_type", 'Not Found'))
        self.ui.license_expire_status.setText(self.license_data.get("expiry", 'No Date Found'))
        self.ui.credit_type_status.setText(self.license_data.get("reset_mode", 'No Type'))
        self.ui.reset_time_status.setText(self.license_data.get("next_reset", 'Not Found'))
        self.ui.credit.setText(str(self.license_data.get('credit', '0')))

    def get_mac_address(self):
        return ':'.join(['{:02x}'.format((uuid.getnode() >> bits) & 0xff)
                         for bits in range(0, 2 * 6, 2)][::-1]).upper()

    def get_local_ip(self):
        try:
            return socket.gethostbyname(socket.gethostname())
        except:
            return "Unknown IP"

    def open_url(self, url):
        QDesktopServices.openUrl(QUrl(url))

    def load_credit(self):
        latest_data = view_license()
        if latest_data:
            self.ui.credit.setText(str(latest_data.get('credit', '0')))

    def get_location(self):
        try:
            response = requests.get(f"http://ip-api.com/json/{self.ip_address}", timeout=5).json()
            if response.get('status') == 'success':
                location = f"{response.get('city', '')}, {response.get('countryCode', '')}"
                self.ui.location.setText(location)
            else:
                self.ui.location.setText("Unknown Location")
        except:
            self.ui.location.setText("Unknown Location")

    def load_notifications(self):
        """Refresh notification UI."""
        notifications = self.session.query(Notification).order_by(Notification.time.desc()).limit(8).all()

        for i, (frame, title_label, time_label) in enumerate(self.notification_frames):
            if i < len(notifications):
                notification = notifications[i]
                title_label.setText(f"⮞ {notification.message}")

                time_diff = datetime.now() - notification.time
                days = time_diff.days
                hours, remainder = divmod(time_diff.seconds, 3600)
                minutes, _ = divmod(remainder, 60)

                if days > 0:
                    time_str = f"{days} day{'s' if days > 1 else ''}, {hours} hour{'s' if hours != 1 else ''}"
                elif hours > 0:
                    time_str = f"{hours} hour{'s' if hours != 1 else ''}, {minutes} minute{'s' if minutes != 1 else ''}"
                elif minutes > 0:
                    time_str = f"{minutes} minute{'s' if minutes != 1 else ''}"
                else:
                    time_str = "Just now"

                time_label.setText(f"{time_str} ago" if time_str != "Just now" else time_str)
                frame.show()
            else:
                frame.hide()

    def closeEvent(self, event):
        self.session.close()
        super().closeEvent(event)
