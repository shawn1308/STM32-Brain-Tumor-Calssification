import serial
from PIL import Image
from numpy import asarray
import numpy as np

ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM10'
ser.open()

#image = Image.open('im_300.jpg')
#numpydata = asarray(image)
#x = numpydata.reshape(-1)

# ARRAY NUMPY -------------------------------------
#arr = np.random.randint(0, 100, size=7)
#values = bytearray(arr.tolist())
#ser.write(values)
#--------------------------------------------------

# IMAGE SEND -------------------------------------
image = Image.open('im_55.jpg')
image = image.convert("L") # Convert the image to grayscale
numpydata = asarray(image)
x = numpydata.reshape(-1) #2D to 1D 
values = bytearray(x.tolist())
ser.write(values)
#--------------------------------------------------


while ser.in_waiting == 0:
    pass
data = ser.read(ser.in_waiting)
print(data.decode())

ser.close() 