import serial
import time
import psutil
ser = serial.Serial("COM3")
file = open("rgb.txt", "w")
file.write("a")
file.close()

mode = 2

pattern = [
    [255, 0, 0],
    [255, 127, 0],
    [255, 255, 0],
    [127, 255, 0],
    [0, 255, 0],
    [0, 255, 127],
    [0, 255, 255],
    [0, 127, 255],
    [0, 0, 255],
    [127, 0, 255],
    [255, 0, 255],
    [255, 0, 127]]
    

def set_all(r, g, b):
    file = open("rgb.txt", "r")
    #print(file.read())
    if file.readline(1) == 'a':
        print("On", file.readline())
        rs = str(round(r, 0))
        if len(rs) == 1:
            rs = '00' + rs
        elif len(rs) == 2:
            rs = '0' + rs
        gs = str(round(g, 0))
        if len(gs) == 1:
            gs = '00' + gs
        elif len(rs) == 2:
            gs = '0' + gs
        bs = str(round(b, 0))
        if len(bs) == 1:
            bs = '00' + bs
        elif len(bs) == 2:
            bs = '0' + bs
        send = 'r' + rs + 'g' + gs + 'b' + bs + '\r\n'
        ser.write(bytes(send, "utf8"))
    else:
        print("off")
        send = 'r000g000b000\r\n'
        ser.write(bytes(send, "utf8"))
    file.close()

while True and mode == 0:
    for cpu_usage in range(100):
        print(cpu_usage)
        set_all(cpu_usage, 0, 100 - cpu_usage)
        time.sleep(0.01)
    for cpu_usage in range(100, 0, -1):
        print(cpu_usage)
        set_all(cpu_usage, 0, 100 - cpu_usage)
        time.sleep(0.01)
    

while True and mode == 1:
    set_all(0, 0, 0)
    
while True and mode == 2:
    set_all(0, 0, 50)

while True and mode == 3:
    for i in pattern:
        set_all(i[0], i[1], i[2])
        time.sleep(0.1)




