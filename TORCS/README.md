# TORCS micro:bit Controller

This project aims at providing a thorough tutorial about how to enable
micro:bit controller on a car racing game - [TORCS](http://torcs.sourceforge.net/).

The purpose of this tutorial is to provide essential knowledge about:

1. How to **program** micro:bit and **read** values from sensors to host PC through **serial port**
2. How a car racing game works
3. How to alter game source code (especially TORCS) to enable micro:bit controller

## Environment Requirements

This tutorial is proven to work on Linux (Ubuntu 16.04 LTS).

To successfully compile TORCS, you need to satisfy the requirements listed in
TORCS official [description](http://torcs.sourceforge.net/index.php?name=Sections&op=viewarticle&artid=3#dependencies).

Since we program micro:bit in C to boost its performance,
please follow the [documentation](https://lancaster-university.github.io/microbit-docs/offline-toolchains/)
of **micro:bit runtime** provided by Lancaster University.

## Installation Instructions

This tutorial contains an example micro:bit TORCS controller.
You can install it to micro:bit by running the `deploy` script under `example`.
In case you don't want to install the native C development environment,
you can directly copy the `example.hex` file to your micro:bit device.

To install TORCS, since its codebase is quite large,
we provide a [link]() for you to download and compile.
This archived file provides essential logic related to micro:bit control,
and you can simply use `sudo make install` to install it.

If your system is different from Ubuntu 16.04 LTS or you would like
to enable more features,
please run `make clean` and then rebuild it by `./configure && make`.

In the codebase we pre-defined the serial port to micro:bit as `/dev/ttyACM0`.
Please revise it if necessary.

