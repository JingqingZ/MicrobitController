# Neverball for micro:bit

## Changes

This is a version of Neverball that supports micro:bit as a controller.

It uses micro:bit's accelerometer as a gyroscope to adjust the angle of the floor.

Video demonstrations
[Video 1](https://www.youtube.com/watch?v=hTfFDC1JrFI) 
[Video 2](https://www.youtube.com/watch?v=nzTZKqwdBv8) 

The changes are only in the files game_server.c game_server.h and st_play.c. The default path for serial output is "/dev/ttyACM0". You can change this value in game_server.h.

An additional file has been added, microbit-neverball.py. It is to be uploaded to the connected micro:bit.
 
Philippos Papaphilippou - Sat Oct 21 20:08:06 BST 2017 - same license 

Notes:
* Remember to callibrate the micro:bit after connecting
* It does not have a proper menu dedicated to micro:bit yet
* Tested in Fedora 26 (4.12.14-300.fc26.x86_64).
* The following information originate from Neverball's original readme.

## Neverball

Tilt the  floor to roll a  ball through an obstacle  course within the
given  time.  If  the  ball falls  or time  expires, a ball is lost.

Collect coins to unlock the exit  and earn extra balls.  Red coins are
worth 5.  Blue coins are worth 10.  A ball is awarded for 100 coins.

## Release Notes

Release highlights can be found in [doc/release-notes.md](doc/release-notes.md).

## Documentation

* [LICENSE.md](LICENSE.md): a description of licensing and exceptions
* [doc/install.txt](doc/install.txt): instructions on how to build the
  game from source code
* [doc/manual.txt](doc/manual.txt): a detailed description of how to
  play and configure the game
* [doc/authors.txt](doc/authors.txt): a list of people who have
  contributed to Neverball

## Resources

* [Website](http://neverball.org/)
* [Development](http://github.com/Neverball)
* [Neverforum](http://neverforum.com/)
* [Nevertable](http://table.nevercorner.net/) (high-score and replay
  database)
* [#neverball on chat.freenode.net](http://webchat.freenode.net/)

## Translation

Neverball uses the gettext approach to translations. We're always
interested in covering more languages. We have a project on Transifex
(see [instructions on the forum][tx]) and we also accept PO files.

[tx]: http://neverforum.com/fmpbo/viewtopic.php?id=2741
