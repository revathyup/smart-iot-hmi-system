import json
import paho.mqtt.client as mqtt

BROKER = "localhost"
PORT = 1883
TOPIC = "home/thermostat/data"
SETPOINT = 22  # Desired temperature

def on_message(client, userdata, msg):
    data = json.loads(msg.payload.decode())
    temp = data["temperature"]
    print(f"Received Temp: {temp:.1f}°C")

    if temp > SETPOINT:
        print("HVAC: Cooling ON")
    else:
        print("HVAC: Heating ON")

client = mqtt.Client()
client.on_message = on_message
client.connect(BROKER, PORT, 60)
client.subscribe(TOPIC)
client.loop_forever()

