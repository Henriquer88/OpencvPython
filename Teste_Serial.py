import serial


ser = serial.Serial('COM20', 115200,bytesize=8,timeout=1)	#Configurando e abrindo a port
print(ser.name)
ser.write(b'L')
ser.close()

