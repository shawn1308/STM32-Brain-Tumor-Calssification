import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        left = QVBoxLayout()
        left.addWidget(QPushButton('Button 1'))
        left.addWidget(QPushButton('Button 2'))
        left.addStretch()
        hbox.addLayout(left,1)

        right = QVBoxLayout()
        right.addWidget(QPushButton('Button 3'))
        right.addWidget(QPushButton('Button 4'))
        right.addWidget(QPushButton('Button 5'))
        right.addWidget(QPushButton('Button 6'))
        right.addStretch()
        hbox.addLayout(right,3)

        self.setLayout(hbox)

        self.setGeometry(300, 300, 600, 200)
        self.setWindowTitle('Two Horizontal Layouts')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
