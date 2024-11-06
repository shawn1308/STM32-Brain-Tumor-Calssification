import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import serial.tools.list_ports
import serial
from PIL import Image
from numpy import asarray
import numpy as np


class Example(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout(self)

# GAUCHE layout (COM port connection)------------------------------------------
        
        left = QVBoxLayout()
        left.addStretch()
        tit_conn = QLabel('Connection')
        tit_conn.setAlignment(Qt.AlignCenter)
        tit_conn.setFont(QFont('Times font', 18))
        tit_conn.setStyleSheet("color: Red") 
        left.addWidget(tit_conn)
        
        # Search COM avaible --------------------------
        self.ports = []
        for port in serial.tools.list_ports.comports():
            self.ports.append(port.name)
        # Selection COM--------------------------------
        txt_com_port = QLabel('PORT:')
        self.com_box = QComboBox()
        self.com_box.addItems(self.ports)
        
        com_hbox = QHBoxLayout()
        com_hbox.addWidget(txt_com_port)
        com_hbox.addWidget(self.com_box)
        
        #com_hbox.addStretch()
        #left.addStretch()
        left.addLayout(com_hbox,1)
        
        # selection BAUD-------------------------------
        txt_baud_port = QLabel('BAUD:')
        self.baud_box = QComboBox() 
        self.baud_box.addItem("115200")
        self.baud_box.addItem("9600")
        
        baud_hbox = QHBoxLayout()
        baud_hbox.addWidget(txt_baud_port)
        baud_hbox.addWidget(self.baud_box)
        
        #baud_hbox.addStretch()
        #left.addStretch()
        left.addLayout(baud_hbox,1)
        
        # selection DATA-------------------------------
        txt_data_port = QLabel('DATA:')
        self.data_box = QComboBox() 
        self.data_box.addItem("8")
        self.data_box.addItem("7")
        
        data_hbox = QHBoxLayout()
        data_hbox.addWidget(txt_data_port)
        data_hbox.addWidget(self.data_box)
        
        #data_hbox.addStretch()
        #left.addStretch()
        left.addLayout(data_hbox,1)
        
        # selection STOP-------------------------------
        txt_stop_port = QLabel('STOP:')
        self.stop_box = QComboBox() 
        self.stop_box.addItem("1")
        self.stop_box.addItem("2")
        
        stop_hbox = QHBoxLayout()
        stop_hbox.addWidget(txt_stop_port)
        stop_hbox.addWidget(self.stop_box)
        
        #stop_hbox.addStretch()
        #left.addStretch()
        left.addLayout(stop_hbox,1)
        
        # selection PARITY-------------------------------
        txt_pari_port = QLabel('PARITY:')
        self.pari_box = QComboBox() 
        self.pari_box.addItem("NONE")
        
        pari_hbox = QHBoxLayout()
        pari_hbox.addWidget(txt_pari_port)
        pari_hbox.addWidget(self.pari_box)
        
        #pari_hbox.addStretch()
        #left.addStretch()
        left.addLayout(pari_hbox,1)
        
        # BUTTON CONNECT ----------------------------------
        self.conn_button = QPushButton('CONNECT')
        self.conn_button.setStyleSheet("color: Red")
        left.addWidget(self.conn_button)
        self.conn_button.clicked.connect(self.connect_button_clicked)
        
        # BUTTON REFRESH ----------------------------------
        
        self.refresh_button = QPushButton('REFRESH')
        left.addWidget(self.refresh_button)
        self.refresh_button.clicked.connect(self.refresh_button_clicked)
        
        # BUTTON DISCONNECT ----------------------------------
        self.disconn_button = QPushButton('DISCONNECT')
        self.disconn_button.setStyleSheet("color: Red")
        left.addWidget(self.disconn_button)
        self.disconn_button.clicked.connect(self.disconnect_button_clicked)
        
        # STATUS ------------------------------------------
        self.status_conn = QLabel('STATUS')
        self.status_conn.setAlignment(Qt.AlignCenter)
        self.status_conn.setFont(QFont('Times font', 13))
        self.status_conn.setStyleSheet("color: Red;background-color: lightgreen")
        left.addWidget(self.status_conn)
        
        
        left.addStretch()
        hbox.addLayout(left,1)

# DROITE layout (INTERFACE)----------------------------------------------------

        right = QVBoxLayout()
        # Les 2 images -----------------------------------------------
        self.ser = serial.Serial()


        with Image.open("sh.jpg") as im:
            # Resize the image to 50x50
            resized_im = im.resize((300, 300))
            # Save the resized image
        resized_im.save("re_im.jpg")

        self.in_img = QLabel(self)
        self.in_img.setAlignment(Qt.AlignCenter)
        self.out_img = QLabel(self)
        self.out_img.setAlignment(Qt.AlignCenter)
        self.pixmap_in = QPixmap('re_im.jpg')
        self.pixmap_out = QPixmap('re_im.jpg')

        self.in_img.setPixmap(self.pixmap_in)
        self.out_img.setPixmap(self.pixmap_out)
    
        self.in_img.resize(50,50)
        self.out_img.resize(50,50)

        im_hbox = QHBoxLayout()
        im_hbox.addWidget(self.in_img)
        im_hbox.addWidget(self.out_img)

        right.addLayout(im_hbox,1)

        # BROWSE et SEND button ------------------------------------
        self.brw_button = QPushButton('BROWSE')
        self.brw_button.setStyleSheet("color: blue")
        self.brw_button.clicked.connect(self.browse_button_clicked)

        self.send_button = QPushButton('SEND')
        self.send_button.setStyleSheet("color: blue")
        self.send_button.clicked.connect(self.send_button_clicked)

        sdbt_hbox = QHBoxLayout()
        sdbt_hbox.addWidget(self.brw_button)
        sdbt_hbox.addWidget(self.send_button)
        right.addLayout(sdbt_hbox,1)

        # OUTPUT label ---------------------------------------------

        self.out_lab = QLabel('OUTPUT')
        self.out_lab.setAlignment(Qt.AlignCenter)
        self.out_lab.setFont(QFont('Times font', 18))
        self.out_lab.setStyleSheet("color: Red") 
        right.addWidget(self.out_lab)

        right.addStretch()
        hbox.addLayout(right,3)
        
        
# Affichage -------------------------------------------------------------------
        self.setLayout(hbox)
        self.setGeometry(400, 400, 800, 400)
        self.setWindowTitle('SERIAL PORT IMAGE SENDER')
        self.show()

# REFRESH les PORTS COM -------------------------------------------------------
    def refresh_button_clicked(self):
        self.ports.clear()
        self.com_box.clear()
        for port in serial.tools.list_ports.comports():
            self.ports.append(port.name)
        self.com_box.addItems(self.ports)
        
# CONNECT les PORTS COM -------------------------------------------------------
    def connect_button_clicked(self):
        self.ser.baudrate = self.baud_box.currentText()
        self.ser.port = self.com_box.currentText()
        self.ser.bytesize = int(self.data_box.currentText())
        self.ser.stopbits = int(self.stop_box.currentText())
        if self.pari_box.currentText() == 'NONE':
            self.ser.parity = 'N'
        self.ser.open()
        print(self.ser.is_open)
        if self.ser.is_open:
            self.status_conn.setText("CONNECTED")
        else:
            self.status_conn.setText("BROKEN")
            
        
# DISCONNECT COMMUNICATION ----------------------------------------------------
    def disconnect_button_clicked(self):
        self.ser.close()
        if self.ser.is_open:
            self.status_conn.setText("CONNECTED")
        else:
            self.status_conn.setText("STATUS")
        
# BROWSE cliqued --------------------------------------------------------------
    
    def browse_button_clicked(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', 
         'c:\\',"Image files (*.jpg *.gif)")
        print(fname[0])
        with Image.open(fname[0]) as im:
            # Resize the image to 50x50
            im_300 = im.resize((256, 256))
            # Save the resized image
            im_300.save("im_256.jpg")
            im_55 = im.resize((55, 55))
            im_55 = im_55.convert("L")
            im_55.save("im_55.jpg")

        self.pixmap_inx = QPixmap('im_256.jpg')
        self.in_img.setPixmap(self.pixmap_inx)

        self.pixmap_outx = QPixmap('im_55.jpg')
        self.out_img.setPixmap(self.pixmap_outx)




 # SEND cliqued -------------------------------------------------------------- 
          
    def send_button_clicked(self):
        image = Image.open('im_55.jpg')
        #image = image.convert("L")
        numpydata = asarray(image)
        x = numpydata.reshape(-1)
        values = bytearray(x.tolist())
        self.ser.write(values)
        while self.ser.in_waiting == 0:
            pass
        # Read the data
        data = self.ser.read(8)
        print(data.decode())
        self.out_lab.setText(data.decode())
        self.status_conn.setText("STATUS")
        self.ser.close() 

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
