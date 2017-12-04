# Gaming Controllers with micro:bit(s)

In this collection of projects, we aim to program [Micro:bit](http://microbit.org) as a controller for games or simulators.

![2 gamers playing SuperTuxKart with wireless micro:bits](https://github.com/JingqingZ/MicrobitController/blob/master/featured-image.jpg)

Team members: Nadeen Gebara, Philippos Papaphilippou, Jingqing Zhang, Ruizhe Zhao (order by surname)

## Modified Games

### Application 1: Neverball

Programmer: Philippos Papaphilippou

"Tilt the floor to roll a ball through an obstacle course within the given time." [Neverball](https://neverball.org/)

This is a version of Neverball that supports micro:bit as a controller. It uses micro:bit's accelerometer as a gyroscope to adjust the angle of the floor. See the project's Readme description for more details and information on how to run.

* Source code: [Neverball for micro:bit](https://github.com/pphilippos/Neverball-for-micro-bit)
* Video: [Controlling Neverball with micro:bit](https://www.youtube.com/watch?v=hTfFDC1JrFI), [close-up](https://www.youtube.com/watch?v=nzTZKqwdBv8)

### Application 2: TORCS

Programmer: Ruizhe Zhao

* Source code: [TORCS](TORCS/)
* Video: [Controlling TORCS with micro:bit](https://www.youtube.com/watch?v=RPB93Nunz84)

### Application 3: AirSim

Programmer: Jingqing Zhang

In this project, we use Micro:bit to control a car/drone based on [AirSim](https://github.com/Microsoft/AirSim).

* Source code: [AirSimController](AirSimController/)
* Videos: [Driving a Car](https://youtu.be/zstsjKxvT5Q), [Driving a Drone](https://youtu.be/9aTPj4cjNWE)

#### Build
* Follow the [installation guide](https://github.com/Microsoft/AirSim) to set up the Unreal Engine and AirSim project.
* [Encode and run](https://www.microbit.co.uk/device/usb) the script [`microbit_code.hex`](AirSimController/microbit_code.hex)(Javacript [`microbit_code.js`](AirSimController/microbit_code.js)) on Micro:bit and keep the Micro:bit connected by USB.
* Run the AirSim project (drone by default or [choosing a car](https://github.com/Microsoft/AirSim/blob/master/docs/using_car.md)).
* Run the corresponding controller script ([`drone_controller.py`](AirSimController/drone_controller.py) or [`car_controller.py`](AirSimController/car_controller.py)) in the source code

## Generic Controllers

### 1. Single/Multi-player wireless gaming for games with keyboard support (Linux)

Programmer: Philippos Papaphilippou

This project maps actions on wirelessly-connected micro:bits to keyboard events. In this way, a variety of multi-player games can be adapted without the need to modify their source code. As a test case we used [SuperTuxKart](https://supertuxkart.net/Main_Page). See the featured image above, or the video below.

* Source code: [GenericLinuxController](https://github.com/pphilippos/Wireless-Gaming-with-micro-bits)
* Video: [Multi-player wireless gaming with micro:bits](https://www.youtube.com/watch?v=YR-1VejseQA)

#### Files 
* microbit-client.py Uploaded to the micro:bit of each player for wireless gaming
* microbit-server.py Uploaded to the micro:bit connected to the PC
* linux-keyboard.c Translates the serial output of the micro:bit server to keyboard events (Requires the libXtst-devel package or equivalent)
(see the source code comments for more information)
  
### 2. Implementation for online games (Bubble Trouble) and Multi-player modification (Windows)
Programmer: Nadeen Gebara

In this project, we use Bubble Trouble as an example to show how a generic controller for online games (single/multi-player) can be created using micro:bit(s).

* Online Game: [Link](https://www.miniclip.com/games/bubble-trouble/en/#t-sd)
* Game details: [Readme](https://github.com/JingqingZ/MicrobitController/blob/master/Bubble_Trouble/Readme.txt)
* Video: [Bubble Trouble Control with Micro:bit](https://www.youtube.com/watch?v=IXL3BHeTE38)



