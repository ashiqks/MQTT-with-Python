
# coding: utf-8

# In[ ]:


#slurry_sensors_emulator.py

from config import *
import paho.mqtt.client as mqtt
import time
import csv
def on_connect(client, userdata, flags, rc):
    print("Result from connect: {}".format(mqtt.connack_string(rc)))
    # Check whether the result form connect is the CONNACK_ACCEPTED connack code
    if rc != mqtt.CONNACK_ACCEPTED:
        raise IOError("Couldn't establish a connection with the MQTT server")
def publish_value(client, topic, value):
    result = client.publish(topic=topic, payload=value, qos=2)
    return result
if __name__ == "__main__":
    client = mqtt.Client(protocol=mqtt.MQTTv311)
    client.on_connect = on_connect
    client.connect(host="broker.hivemq.com", port=1883)
    client.loop_start()
    print_message = "{}: {}"
   
    while True:
        with open('slurry_data.csv') as csvfile:
            reader=csv.reader(csvfile)
            for row in reader:
                level_value = float(row[0])
                methane_value = float(row[1])
                print(print_message.format(level_topic, level_value))
                print(print_message.format(methane_topic, methane_value))
                publish_value(client, level_topic, level_value)
                publish_value(client, methane_topic, methane_value)
                time.sleep(1)
 
    client.disconnect()
    client.loop_stop()

