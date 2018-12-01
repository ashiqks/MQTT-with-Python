
# coding: utf-8

# In[ ]:


#slurry_monitor.py
from slurry_config import *
import paho.mqtt.client as mqtt
import time
import json
mqtt_host = "broker.hivemq.com"

class Slurry:
    active_instance = None
    
    def __init__(self, level, methane_value):
        self.level = level
        self.methane_value = methane_value
        Slurry.active_instance = self
        
        
def on_connect_mosquitto(client, userdata, flags, rc):
    print("Result from Mosquitto connect: {}".format(
        mqtt.connack_string(rc)))
    # Check whether the result form connect is the CONNACK_ACCEPTED  connack code
    if rc == mqtt.CONNACK_ACCEPTED:
        # Subscribe to a topic filter that provides all the sensors
        sensors_topic_filter = topic_format.format(slurry_name, "+")
        client.subscribe(sensors_topic_filter)
        
def on_subscribe_mosquitto(client, userdata, mid, granted_qos):
    print("I've subscribed")
    
def print_received_message_mosquitto(msg):
    print("Message received. Topic: {}. Payload: {}".format(msg.topic, str(msg.payload)))
    
def on_level_message_mosquitto(client, userdata, msg):
    print_received_message_mosquitto(msg)
    Slurry.active_instance.level = float(msg.payload)
    
def on_methane_message_mosquitto(client, userdata, msg):
    print_received_message_mosquitto(msg)
    Slurry.active_instance.methane_value = float(msg.payload)
    
if __name__ == "__main__":
    slurry = Slurry(level=0, methane_value=0) 
    mosquitto_client = mqtt.Client(protocol=mqtt.MQTTv311)
    mosquitto_client.on_connect = on_connect_mosquitto
    mosquitto_client.on_subscribe = on_subscribe_mosquitto
    mosquitto_client.message_callback_add(level_topic, on_level_message_mosquitto)
    mosquitto_client.message_callback_add(methane_topic, on_methane_message_mosquitto)
    mosquitto_client.connect(host=mqtt_host, port=1883)
    mosquitto_client.loop_forever()

