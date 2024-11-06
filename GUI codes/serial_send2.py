import serial
ser = serial.Serial()
ser.baudrate = 115200
ser.port = 'COM10'
ser.open()
data_array = [1, 4, 7, 12, 45, 78, 91]
values = bytearray(data_array)
ser.write(values)
ser.close() 