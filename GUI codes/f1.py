import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(1400, 800)
        self.setWindowTitle("PyQt5")

        b1 = QPushButton("Button1")
        b2 = QPushButton("Button2")

        vbox = QVBoxLayout()
        vbox.addWidget(b1)
        vbox.addStretch()
        vbox.addWidget(b2)

        layout1 = QHBoxLayout()
        layout1.addLayout(vbox)
        layout1.setContentsMargins(0, 0, 0, 0)
        layout1.setSpacing(0)
        

        layout2 = QHBoxLayout()
        layout2.addLayout(vbox)
        layout2.setContentsMargins(0, 0, 0, 0)
        layout2.setSpacing(0)

        layout = QHBoxLayout()
        layout.addLayout(layout1, 1)
        layout.addLayout(layout2, 3)

        self.setLayout(layout)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
