#include <lorawan.h>
#include "Lora.h"

//This line updates which node the code is for, by changing it you can have multiple devices 
int node = BOARD_FIVE;

const char *devAddr = nodeArray[node].devAddr;
const char *nwkSKey = nodeArray[node].nwkSKey;
const char *appSKey = nodeArray[node].appSKey;

char myStr[50];
char outStr[255];

//Physical Pinout for tower board
const sRFM_pins RFM_pins = {
  .CS = 10,
  .RST = 9,
  .DIO0 = 2,
  .DIO1 = 6,
  .DIO2 = 7,
  .DIO5 = 15,
};

byte recvStatus = 0;

void loraSetup(){
    while(!Serial);
  if(!lora.init()){
    Serial.println("RFM95 not detected");
    delay(5000);
    return;
  }

  // Set LoRaWAN Class change CLASS_A or CLASS_C
  lora.setDeviceClass(CLASS_A);

  // Set Data Rate
  lora.setDataRate(SF9BW125);

  // set channel to random
  lora.setChannel(MULTI);
  
  // Put ABP Key and DevAddress here
  lora.setNwkSKey(nwkSKey);
  lora.setAppSKey(appSKey);
  lora.setDevAddr(devAddr);
}

//Convert the sensor data array into a string for sending
String convert(float a[8]) {
  String msg8 = "";
  for (int i = 0; i < 8; i++) {
    String msg = String(a[i]);
    msg8 += msg;
    if (i < 7) {
      msg8 += " ";
    }
  }

  return msg8;
}

//Sends a type Data object containing sensor output to the gateway
void sendMsg(Data data_in) {

  float data[8] = { data_in.massConcentrationPm1p0, data_in.massConcentrationPm2p5, data_in.massConcentrationPm4p0,
                    data_in.massConcentrationPm10p0, data_in.ambientHumidity, data_in.ambientTemperature, data_in.vocIndex };

  data[8] = (float)node;

  String msg = convert(data);

  char msg_char[52];
  msg.toCharArray(msg_char, msg.length());

  // Check interval overflow
  //if (millis() - previousMillis > interval) {
  previousMillis = millis();

  lora.sendUplink(msg_char, strlen(msg_char), 0, 1);
  // }

  recvStatus = lora.readData(outStr);
  //If receive status is confirmed from gateway printout sent data
  if (recvStatus) {
   // Serial.println(outStr);
  }
}
