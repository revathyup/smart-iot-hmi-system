import pandas as pd
import matplotlib.pyplot as plt

LOG_FILE = "data/sensor_log.csv"

# Load data
df = pd.read_csv(LOG_FILE, parse_dates=["timestamp"])

plt.figure(figsize=(10,5))
plt.plot(df["timestamp"], df["temperature"], label="Temperature (°C)")
plt.plot(df["timestamp"], df["humidity"], label="Humidity (%)")
plt.xlabel("Time")
plt.ylabel("Values")
plt.title("Smart Thermostat Data Log")
plt.legend()
plt.grid(True)
plt.show()

