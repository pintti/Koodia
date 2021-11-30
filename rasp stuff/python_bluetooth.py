import serial
with serial.Serial('COM5', 9600, timeout=10) as ser:
    print("lol")
    x = ser.read()          # read one byte
    #s = ser.read(10)        # read up to ten bytes (timeout)
    #line = ser.readline()
    print(x)