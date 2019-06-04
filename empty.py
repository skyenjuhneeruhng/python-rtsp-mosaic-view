from ui_empty import Ui_wEmpty
from PyQt5 import QtWidgets

class wEmpty(QtWidgets.QWidget, Ui_wEmpty):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
