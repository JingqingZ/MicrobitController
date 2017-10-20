#-*- code: utf-8 -*-

import ast
import serial

serialPort = serial.Serial("/dev/ttyACM0", 115200)

def parseAcc(msg):
    msg = msg.decode("ascii")
    msg = msg[:-2]
    try:
        acc = ast.literal_eval(msg)
    except Exception as e:
        print(e)
        return dict()
    return acc

def readSerial():
    msg = serialPort.readline()
    acc = parseAcc(msg)
    # print(acc)
    return acc

if __name__ == "__main__":
    while True:
        ser = readSerial()
        print(ser)
