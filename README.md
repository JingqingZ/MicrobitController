# MicrobitController

Team members: Nadeen Gebara, Philippos Papaphilippou, Jingqing Zhang, Ruizhe Zhao (order by surname)

In this collection of projects, we aim to program [Micro:bit](http://microbit.org) as a controller for games or simulators.

## Modified Games

### Application 1: Neverball

Programmer: Philippos Papaphilippou

### Application 2: TORCS

Programmer: Ruizhe Zhao

### Application 3: AirSim

Programmer: Jingqing Zhang

In this project, we use Micro:bit to control a car/drone based on [AirSim](https://github.com/Microsoft/AirSim).

* Source code: [AirSimController/](AirSimController/)
* Videos: [Driving a Car](https://youtu.be/zstsjKxvT5Q), [Driving a Drone](https://youtu.be/9aTPj4cjNWE)

#### Build
* Follow the [installation guide](https://github.com/Microsoft/AirSim) to set up the Unreal Engine and AirSim project.
* [Encode and run](https://www.microbit.co.uk/device/usb) the script [`microbit_code.hex`](AirSimController/microbit_code.hex)(Javacript [`microbit_code.js`](AirSimController/microbit_code.js)) on Micro:bit and keep the Micro:bit connected by USB.
* Run the AirSim project (drone by default or [choosing a car](https://github.com/Microsoft/AirSim/blob/master/docs/using_car.md)).
* Run the corresponding controller script ([`drone_controller.py`](AirSimController/drone_controller.py) or [`car_controller.py`](AirSimController/car_controller.py)) in the source code

## Generic Controllers

### 1. Single/Multi-player wireless gaming for games with keyboard support (Linux Version)
Programmer: Philippos Papaphilippou

### 2. Windows implementation for online games (Bubble Trouble) and Multi-player modification
Programmer: Nadeen Gebara

## Video Demonstrations
(or where they belong)

