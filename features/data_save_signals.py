# features/data_save_signals.py
from PyQt6.QtCore import QObject, pyqtSignal

class AppSignals(QObject):
    credit_saved = pyqtSignal()
    license_saved = pyqtSignal()
    notification_saved = pyqtSignal()
    data_saved = pyqtSignal()

    def __init__(self):
        super().__init__()  # VERY important!

# Create ONE shared instance
signals = AppSignals()
