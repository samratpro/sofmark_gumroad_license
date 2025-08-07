from PyQt6.QtGui import QFontDatabase, QFont

from pages.homePage import homepage
from ui.dashboard_ui import Ui_MainWindow
from PyQt6.QtWidgets import QMainWindow, QWidget
from pages.licensePage import licensePage

class DashboardPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_ui()
        self.setup_fonts()

    def setup_fonts(self):
        font_regular_id = QFontDatabase.addApplicationFont("font/OpenSans-Regular.ttf")
        font_regular = QFont(QFontDatabase.applicationFontFamilies(font_regular_id)[0], 11)
        self.apply_font_to_all_widgets(font_regular)
    def apply_font_to_all_widgets(self, font: QFont):
        for widget in self.findChildren(QWidget):
            widget.setFont(font)

    def setup_ui(self):
        # ************  Home Page -- top part
        print("debug HomePage")
        self.homePage = homepage()
        self.ui.stackedWidget.addWidget(self.homePage)



        # ************ settings page -- Bottom part
        print("debug licensePage")
        self.licensePage = licensePage("self.username")
        self.ui.stackedWidget.addWidget(self.licensePage)
        print("debug after licensePage")
        # End pages ***********************
        # Page switching
        try:
            self.ui.homeIconBtn.clicked.connect(lambda: self.switch_page("home"))
            self.ui.homeBtn.clicked.connect(lambda: self.switch_page("home"))


            self.ui.licenseBtn.clicked.connect(lambda: self.switch_page("license_page"))
            self.ui.licenseIconBtn.clicked.connect(lambda: self.switch_page("license_page"))

        except AttributeError as e:
            print(f"Error connecting button: {e}")

    def switch_page(self, page_name):
        try:
            if page_name == "home":
                self.ui.stackedWidget.setCurrentWidget(self.homePage)

            elif page_name == "license_page":
                self.ui.stackedWidget.setCurrentWidget(self.licensePage) 
            else:
                print(f"Invalid page name: {page_name}")
        except Exception as e:
            print(f"Error switching page: {e}")
