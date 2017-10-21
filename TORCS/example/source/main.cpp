/**
 * The main entry for the micro:bit game controller.
 */

#include <stdlib.h>
#include <string.h>
#include <math.h>

#include "MicroBit.h"

#define MAX_BUF_SZ 256

MicroBit uBit;

int main() {
  // stream buffer
  char buf[MAX_BUF_SZ];
  // accelerometer
  int X, Y, Z;
  // magnetometer
  int m_X, m_Y, m_Z;
  // buttons
  char btn_A_status, btn_B_status;
  // heading
  int h;

  uBit.init();

  // connected to USB serial ports
  MicroBitSerial serial(USBTX, USBRX);

  // uBit.display.scroll("GAME CONTROLLER!");
  
  // buttons
  MicroBitButton btn_A(
      MICROBIT_PIN_BUTTON_A, MICROBIT_ID_BUTTON_A); 
  MicroBitButton btn_B(
      MICROBIT_PIN_BUTTON_B, MICROBIT_ID_BUTTON_B); 

  // compass
  MicroBitI2C i2c(I2C_SDA0, I2C_SCL0); 

  MicroBitCompass compass(i2c); 

  compass.configure();
  // compass.calibrate();

  // main event loop
  while (true) {
    // access accelerometer
    X = uBit.accelerometer.getX();
    Y = uBit.accelerometer.getY();
    Z = uBit.accelerometer.getZ();

    btn_A_status = (btn_A.isPressed()) ? 'x' : 'o';
    btn_B_status = (btn_B.isPressed()) ? 'x' : 'o';

    // h = compass.heading();

    m_X = compass.getX();
    m_Y = compass.getY();
    m_Z = compass.getZ();
    // h = (int) (atan2((float) m_Y, (float) m_X) * 180 / 3.1415926);

    sprintf(buf, "x%5dy%5dz%5dA%cB%c\n",
        X, Y, Z, btn_A_status, btn_B_status);

    ManagedString s((const char *) buf);
    serial.send(s, SYNC_SPINWAIT);
  }

  release_fiber();

  return 0;
}
