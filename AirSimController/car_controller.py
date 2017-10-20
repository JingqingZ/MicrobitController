import readSerial
from AirSimClient import *


# connect to the AirSim simulator
client = CarClient()
client.confirmConnection()
client.enableApiControl(True)
car_controls = CarControls()

while True:

    # get state of the car
    # car_state = client.getCarState()
    # print("Speed %d, Gear %d" % (car_state.speed, car_state.gear))

    ser = readSerial.readSerial()
    if "button" in ser:
        if ser["button"] == "A":
            # go forward
            car_controls.brake = 0 #remove break
            car_controls.is_manual_gear = False # change back gear to auto
            car_controls.manual_gear = 0
            if car_controls.throttle < 0.5:
                car_controls.throttle = 0.5
            else:
                car_controls.throttle += 0.01
            car_controls.steering = 0
            client.setCarControls(car_controls)
            print("Go Foward")
            # time.sleep(3)   # let car drive a bit
        elif ser["button"] == "B":
            # apply breaks
            car_controls.throttle = 0
            car_controls.brake = 1
            client.setCarControls(car_controls)
            print("Apply break")
            # time.sleep(3)   # let car drive a bit
            # car_controls.brake = 0 #remove break
        elif ser["button"] == "AB":
            # go reverse
            car_controls.brake = 0 #remove break
            car_controls.throttle = -0.5
            car_controls.is_manual_gear = True
            car_controls.manual_gear = -1
            car_controls.steering = 0
            client.setCarControls(car_controls)
            print("Go reverse")
            # time.sleep(3)   # let car drive a bit
    elif "x" in ser:
        # Go forward + steer right
        # car_controls.throttle = 0.5
        car_controls.steering = ser["x"] / 1024
        client.setCarControls(car_controls)
        # print("Steering")
    # time.sleep(3)   # let car drive a bit

#restore to original state
client.reset()

client.enableApiControl(False)
