/* This program is reading the serial output of the micro:bit flashed with
 * microbit-server.py. It translates the wireless micro:bit actions into
 * keyboard events for use in multi-player games.
 *
 * See demonstration video for SuperTuxKart:
 * https://www.youtube.com/watch?v=YR-1VejseQA
 *
 * Compile with: gcc -lX11 -lXtst linux-keyboard.c
 * Required libraries: libXtst-devel (or equivalent)
 * Tested on: Fedora 4.12.14-300.fc26.x86_64
 *
 * Philippos Papaphilippou
 * Sat Oct 21 20:08:06 BST 2017
 * GPLv2
 */

#include <stdio.h>
#include <string.h>
#include <unistd.h>
#include <errno.h>

#include <fcntl.h>
#include <termios.h>

#include <X11/Xlib.h>
#include <X11/keysym.h>
#include <X11/extensions/XTest.h>

int main(void) {

  int fd = open("/dev/ttyACM0", O_RDWR);
  FILE* fp = fdopen(fd,"r");

  Display *display;
  unsigned int keycode;
  display = XOpenDisplay(0);

  char line[256];

  // Association of micro:bit actions to key presses
  // ( You can find a list of possible keydodes here:
  //   https://www.cl.cam.ac.uk/~mgk25/ucs/keysymdef.h )
  int keycodes[4][9] = {{XK_z, XK_x,XK_Right, XK_Left, XK_Down, XK_Up, XK_c, XK_v, XK_b},
  					  {XK_r, XK_t, XK_d, XK_a, XK_s, XK_w, XK_y, XK_u, XK_i},
  					  {XK_5, XK_6,XK_2,XK_1,XK_4,XK_3,XK_7,XK_8,XK_9},
  					  {XK_f, XK_g, XK_m, XK_b, XK_h, XK_n, XK_j, XK_k, XK_l}};

  while(1){
    FILE* fp = fdopen(fd,"r");
  	while(strlen(line)!=10){
  		fscanf(fp,"%s",line);
  		printf("%s\n", line);
  	}
	// It accepts actions from upto 4 players 'A', 'B', 'C' or 'D'
  	int id = line[0]-'A';
  	int i = 0;
  	for (i=0; i<9; i++){
  		keycode = XKeysymToKeycode(display, keycodes[id][i]);
		// The events are either hold or release key.
  		if (line[i+1]=='1'){
  			XTestFakeKeyEvent(display, keycode, True, 0);
  		} else {
  			XTestFakeKeyEvent(display, keycode, False, 0);
  		}
  	}
  	XFlush(display);
  	line[0]='\0';
  }

  return 0;
}
