import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(1400, 800)
        self.setWindowTitle("PyQt5")

        label1 = QLabel('My wonderful application')
        label2 = QLabel('The button:')
        button = QPushButton('Press me!')

        bottom_widget = QWidget()
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(label2)
        bottom_layout.addWidget(button)
        bottom_widget.setLayout(bottom_layout)
        bottom_widget.setFixedSize(500,100)
        label1.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(bottom_widget)
        self.setLayout(layout)

        self.setWindowTitle('My Application')
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
