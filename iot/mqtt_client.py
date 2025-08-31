import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import time
import json
import paho.mqtt.client as mqtt
from sensors.temp_humidity import read_sensor

BROKER = "localhost"
PORT = 1883
TOPIC = "home/thermostat/data"


client = mqtt.Client()

def connect_mqtt():
    client.connect(BROKER, PORT, 60)
    client.loop_start()

def publish_sensor_data():
    while True:
        temp, humidity = read_sensor()
        payload = json.dumps({"temperature": temp, "humidity": humidity})
        client.publish(TOPIC, payload)
        print(f"Published: {payload}")
        time.sleep(2)

if __name__ == "__main__":
    connect_mqtt()
    publish_sensor_data()