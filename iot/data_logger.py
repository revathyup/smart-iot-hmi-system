import json
import csv
import time
import paho.mqtt.client as mqtt
import os

BROKER = "localhost"
PORT = 1883
TOPIC = "home/thermostat/data"
LOG_FILE = "data/sensor_log.csv"

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# Write CSV header if file is empty
if not os.path.exists(LOG_FILE) or os.path.getsize(LOG_FILE) == 0:
    with open(LOG_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["timestamp", "temperature", "humidity"])

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    temp = data["temperature"]
    humidity = data["humidity"]

    with open(LOG_FILE, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), temp, humidity])

    print(f"Logged: {temp:.1f}°C, {humidity:.1f}%")

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)
client.loop_forever()

