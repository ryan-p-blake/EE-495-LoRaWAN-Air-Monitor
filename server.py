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
    #print(parsedJSON)
    data = parsedJSON["uplink_message"]["decoded_payload"]["bytes"]
    node = parsedJSON["end_device_ids"]["device_id"].split('-')[-1] # get the last part of device_id as node number
 
    #print(str(data) + "is the data")

    byte_val = bytes(data);
    str_data = str(byte_val, 'ascii')

    data_list = str_data.split()
    #print(data_list)


    pm1_0 = data_list[0]
    pm2_5 = data_list[1]
    pm4_0 = data_list[2]
    pm10_0 = data_list[3]
    humidity = data_list[4]
    tmp = data_list[5]
    voc = data_list[6]

    # Add the node number to the file name
    pm2_5_filename = "pm2.5_" + node + ".txt"
    pm4_0_filename = "pm4.0_" + node + ".txt"
    pm10_filename = "pm10_" + node + ".txt"
    humidity_filename = "humidity_" + node + ".txt"
    tmp_filename = "tmp_" + node + ".txt"
    voc_filename = "voc_" + node + ".txt"

    # Create a directory named "DataFolder" if it does not exist
    if not os.path.exists("DataFolder"):
        os.makedirs("DataFolder")

    # Write data to the corresponding files in the "DataFolder" directory
    with open(os.path.join("DataFolder", pm2_5_filename), "a") as f:
        f.write(str(pm2_5) + " ")
    with open(os.path.join("DataFolder", pm4_0_filename), "a") as f:
        f.write(str(pm4_0) + " ")
    with open(os.path.join("DataFolder", pm10_filename), "a") as f:
        f.write(str(pm10_0) + " ")
    with open(os.path.join("DataFolder", humidity_filename), "a") as f:
        f.write(str(humidity) + " ")
    with open(os.path.join("DataFolder", tmp_filename), "a") as f:
        tmpC = float(tmp) * 1.8 + 32.0
        tmp = str(round(tmpC,2))
        f.write(str(tmp) + " ")
    with open(os.path.join("DataFolder", voc_filename), "a") as f:
        f.write(str(voc) + " ")

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
 

