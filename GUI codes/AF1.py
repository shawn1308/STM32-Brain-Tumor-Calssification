import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.resize(1400, 800)
        self.setWindowTitle("PyQt5")
        
        hbox = QHBoxLayout(self)
        left = QVBoxLayout()
        right = QVBoxLayout()

        tit_conn = QLabel('Connection')
        
        txt_com_port = QLabel('PORT:')
        com_box = QComboBox() 
        com_box.addItem("HEY") 

        com_connec_widget = QWidget()
        com_connec_layout = QHBoxLayout()
        com_connec_layout.addWidget(txt_com_port)
        com_connec_layout.addWidget(com_box)
        com_connec_widget.setLayout(com_connec_layout)
        left.addLayout(com_connec_layout)
        
        

        hbox.addLayout(left,1)
        hbox.addLayout(right,3)
        self.setLayout(hbox)
        self.show()


def main():
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
