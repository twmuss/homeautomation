#!/usr/bin/env python
import paho.mqtt.client as mqtt
import serial

s = serial.Serial('/dev/ttyUSB0', 9600)

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    client.subscribe("schlafzimmer")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    if ((msg.topic == "schlafzimmer") & (msg.payload == "0")):
	s.write("0")
    if ((msg.topic == "schlafzimmer") & (msg.payload == "1")):
	s.write("1")
    if ((msg.topic == "schlafzimmer") & (msg.payload == "2")):
	s.write("2")
    if ((msg.topic == "schlafzimmer") & (msg.payload == "3")):
	s.write("3")
    if ((msg.topic == "schlafzimmer") & (msg.payload == "4")):
	s.write("4")
    if ((msg.topic == "schlafzimmer") & (msg.payload == "5")):
	s.write("5")
    if ((msg.topic == "schlafzimmer") & (msg.payload == "6")):
	s.write("6")
    if ((msg.topic == "schlafzimmer") & (msg.payload == "7")):
	s.write("7")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("10.1.1.22", 1883, 60)

client.loop_forever()
