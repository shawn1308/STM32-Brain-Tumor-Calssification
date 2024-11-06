import sys
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()

        uic.loadUi("Scre01.ui.ui.qml",self)
        self.show()

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()