#!/usr/bin/python3
 
User = "dragino-shield-app@ttn"
Password = "NNSXS.KCJBDPHP3Z6HGEWXRME4SUCIPYNVWNOVXVIMKSY.Y6QBSYMB5UGPL5GTTILQ76FX7AVCEIBGKPJJNI2ZPVSIDCC74OOQ"
theRegion = 'NAM1'    # The region you are using

#Arrays for data collection
pm1_0 = []
pm2_5 = []
pm4_0 = []
pm10_0 = []
humidity = []
tmp = [] 
voc = []
 

VER  = "2021-05-24 v1.2"
import os, sys, logging, time
print(os.path.basename(__file__) + " " + VER)
 
print("Imports:")
import paho.mqtt.client as mqtt
import json
import csv
from datetime import datetime

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
  
 
# MQTT event functions
def on_connect(mqttc, obj, flags, rc):
    print("\nConnect: rc = " + str(rc))
 
def on_message(mqttc, obj, msg):
    print("\nMessage: " + msg.topic + " " + str(msg.qos)) # + " " + str(msg.payload))
    parsedJSON = json.loads(msg.payload)
    print(parsedJSON)
    data = parsedJSON["uplink_message"]["decoded_payload"]["bytes"]
    node_num = parsedJSON["end_device_ids"]["device_id"].split('-')[-1] # get the last part of device_id as node number
 
    #print(str(data) + "is the data")

    byte_val = bytes(data);
    str_data = str(byte_val, 'ascii')

    data_list = str_data.split()
    print(data_list)


    pm1_0 = data_list[0]
    pm2_5 = data_list[1]
    pm4_0 = data_list[2]
    pm10_0 = data_list[3]
    humidity = data_list[4]
    tmp = data_list[5]
    voc = data_list[6]
    node = data_list[7]
#   SEND TO DATABASE
#   ref.set(data_list)

    
    f = open("pm2.5.txt", "a")
    f.write(str(pm2_5) + " ")
    f.close()
    f = open("pm4.0.txt", "a")
    f.write(str(pm4_0) + " ")
    f.close()
    f = open("pm10.txt", "a")
    f.write(str(pm10_0) + " ")
    f.close()
    f = open("humidity", "a")
    f.write(str(humidity) + " ")
    f.close()
    f = open("tmp.txt", "a")
    tmpC = float(tmp) * 1.8 + 32.0
    tmp = str(round(tmpC,2))
    f.write(str(tmp) + " ")
    f.close()
    f = open("voc.txt", "a")
    f.write(str(voc) + " ")
    f.close()

    #print(json.dumps(parsedJSON, indent=4))    # Uncomment this to fill your terminal screen with JSON
 
def on_subscribe(mqttc, obj, mid, granted_qos):
    print("\nSubscribe: " + str(mid) + " " + str(granted_qos))
 
def on_log(mqttc, obj, level, string):
    print("\nLog: "+ string)
    logging_level = mqtt.LOGGING_LEVEL[level]
    logging.log(logging_level, string)
 
#  # Initialize Firebase SDK
# cred = credentials.Certificate("./vue-http-key.json")
# firebase_admin.initialize_app(cred, {
#     'databaseURL': 'https://vue-http-demo-3f7e6-default-rtdb.firebaseio.com/'
# })

# # Get a reference to the location in the database where you want to store the data
# ref = db.reference('path/to/data_list')
 
 
 
print("Body of program:")
 
print("Init mqtt client")
mqttc = mqtt.Client()
 
print("Assign callbacks")
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.on_message = on_message
#mqttc.on_log = on_log      # Logging for debugging OK, waste
 
print("Connect")
# Setup authentication from settings above
mqttc.username_pw_set(User, Password)
 
 
# IMPORTANT - this enables the encryption of messages
mqttc.tls_set() # default certification authority of the system
 
#mqttc.tls_set(ca_certs="mqtt-ca.pem") # Use this if you get security errors
# It loads the TTI security certificate. Download it from their website from this page:
# https://www.thethingsnetwork.org/docs/applications/mqtt/api/index.html
# This is normally required if you are running the script on Windows
 
 
mqttc.connect(theRegion.lower() + ".cloud.thethings.network", 8883, 60)
 
 
print("Subscribe")
mqttc.subscribe("#", 0) # all device uplinks
 
print("And run forever")


try:    
    run = True
    while run:
        mqttc.loop(10)  # seconds timeout / blocking time
        print(".", end="", flush=True)  # feedback to the user that something is actually happening
        time.sleep(5)
           
except KeyboardInterrupt:
    print("Exit")
    sys.exit(0)
 

