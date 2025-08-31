import tkinter as tk
import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "home/thermostat/data"

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    temp = data["temperature"]
    humidity = data["humidity"]
    temp_label.config(text=f"Temperature: {temp:.1f}°C")
    humidity_label.config(text=f"Humidity: {humidity:.1f}%")

# GUI setup
root = tk.Tk()
root.title("Smart Thermostat HMI")

temp_label = tk.Label(root, font=("Arial", 16))
humidity_label = tk.Label(root, font=("Arial", 16))
temp_label.pack(pady=10)
humidity_label.pack(pady=10)

# MQTT setup
client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)
client.loop_start()

root.mainloop()

