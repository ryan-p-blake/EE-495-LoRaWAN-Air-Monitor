/**
 * Authors:
 * Ryan Blake 
 * Based on modified LMIC Code Beelan-LoRaWAN under the The MIT License

Copyright (c) 2013 Seeed Technology Inc.

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
 
 */

#include <lorawan.h>
#include <Arduino.h>

//data struct 
typedef struct {
  float massConcentrationPm1p0;
  float massConcentrationPm2p5;
  float massConcentrationPm4p0;
  float massConcentrationPm10p0;
  float ambientHumidity;
  float ambientTemperature;
  float vocIndex;
  float noxIndex;
} Data;


const unsigned long interval = 600000;    // Main interval delay to send message, TTN Requires 1 message per 60 seconds approximatley 

unsigned long previousMillis = 0;  // will store last time message sent
unsigned int counter = 0;     // message counter



//print out sensor data 
int print = 0;

void setup() {
  Serial.begin(115200);
  sen54Start();
  loraSetup();
  Data data_in = {0,0,0,0,0,0,0,0};
  

  //Run sensor a few times before going into main loop to warm it up
  for(int i = 0; i < 5; i++){
    data_in = getSen54Data(print);
    delay(500);
  }
}

int printvalues = 0;

void loop() {


  // String data;
  Data data_in = {0,0,0,0,0,0,0,0};
  data_in = getSen54Data(printvalues);
  sendMsg(data_in);
  lora.update();
  delay(1000);
 // delay(interval);

}
