import serial
import csv
import simpleaudio
import time

portname = '/dev/cu.usbmodem141101'
datafolder = "data/"
datafilename = "ecg-recordtest"

ser = serial.Serial(port =portname, baudrate = 115200)

dataList = []
ser.reset_input_buffer()

while True:
    try:
        line = ser.readline().decode("ascii")
        data = [float(d) for d in line.split(",")]
        dataList.append(data)
    except:
        print("keyboard interupt")
        break


with open(datafolder + datafilename+ '.csv', 'w', newline="") as f:
    print(ser.in_waiting)
    csvWriter = csv.writer(f)
    for data in dataList:
        csvWriter.writerow(data)

print('writing finished')

time.sleep(1)
ser.close()
