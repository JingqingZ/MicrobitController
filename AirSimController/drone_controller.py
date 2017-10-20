import readSerial
from AirSimClient import *

# connect to the AirSim simulator
client = MultirotorClient()
client.confirmConnection()
client.enableApiControl(True)
client.armDisarm(True)
client.takeoff()
print("Ready")

start = False

while True:

    ser = readSerial.readSerial()
    if "button" in ser:
        if ser["button"] == "A":
            print("Up")
            client.moveByVelocity(0, 0, -10, 0.01, DrivetrainType.ForwardOnly, YawMode(False, 0))
            start = True
        elif ser["button"] == "B":
            print("Down")
            client.moveByVelocity(0, 0, 10, 0.01, DrivetrainType.ForwardOnly, YawMode(False, 0))
        elif ser["button"] == "AB":
            pass
    elif start and "x" in ser and "y" in ser:
        print("Fly")
        serx = ser["x"] if abs(ser["x"]) > 150 else 0
        sery = ser["y"] if abs(ser["y"]) > 150 else 0
        client.moveByVelocity(-sery // 20, serx // 20, 0, 0.3)
