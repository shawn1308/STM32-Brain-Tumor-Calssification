import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
from PyQt5.QtCore import Qt

class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

        label1 = QLabel('My wonderful application')
        label2 = QLabel('The button:')
        button = QPushButton('Press me!')
        
        bottom_widget = QWidget()
        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(label2)
        bottom_layout.addWidget(button)
        bottom_widget.setLayout(bottom_layout)
        
        widget = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(bottom_widget)
        widget.setLayout(layout)

        self.setLayout(layout)

        self.setGeometry(300, 300, 600, 200)
        self.setWindowTitle('Two Horizontal Layouts')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
