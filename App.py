import sys
import os
from PyQt6.QtCore import Qt
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QIcon, QKeyEvent
from dashboard import DashboardPage
import sys

class Dashboard(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dashboard")
        self.setMinimumSize(1000, 600)

        # Initialize the dashboard UI
        self.dashboard_ui = DashboardPage()
        self.dashboard_ui.ui.setupUi(self)
        self.dashboard_ui.setup_ui()

        # Assuming you have a logout button defined in your UI
        self.dashboard_ui.ui.logoutBtn.clicked.connect(self.handle_exit)
        self.dashboard_ui.ui.logoutIconBtn.clicked.connect(self.handle_exit)

    def handle_exit(self):
        """Handle the logout button click."""
        self.app = QApplication.instance()
        if self.app:
            self.app.quit()


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sofmark")
        self.setMinimumSize(1200, 700)
        self.setWindowIcon(QIcon("images/logo.png"))
        self.show_dashboard()


    def show_dashboard(self):
        try:
            """Switches to the dashboard after a successful login."""
            # Recreate the dashboard
            self.dashboard = Dashboard()
            print("Showing dashboard")
            self.setCentralWidget(self.dashboard)
        except Exception as e: 
            print(f"Error in show_dashboard: {e}")

    def keyPressEvent(self, event: QKeyEvent):
        """
        Override the keyPressEvent to handle F11 for fullscreen toggling.
        """
        if event.key() == Qt.Key.Key_F11:
            # Toggle fullscreen mode
            if self.isFullScreen():
                self.showNormal()  # Exit fullscreen
            else:
                self.showFullScreen()  # Enter fullscreen
        else:
            # Call the base class keyPressEvent for other keys
            super().keyPressEvent(event)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = App()
    main_window.show()
    sys.exit(app.exec())