import random
import time

def read_sensor():
    temp = 20 + random.uniform(-2, 2)
    humidity = 50 + random.uniform(-5, 5)
    return temp, humidity

if __name__ == "__main__":
    while True:
        t, h = read_sensor()
        print(f"Temperature: {t:.1f}°C, Humidity: {h:.1f}%")
        time.sleep(1)
