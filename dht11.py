import Adafruit_DHT
import RPi.GPIO as GPIO
import time

# Define sensor type
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 4  # Physical Pin 12 (BOARD Mode)

# Set GPIO mode to BOARD (physical pin numbering)
#GPIO.setmode(GPIO.BOARD)

#print("Reading DHT11 Sensor Data on Pin 26. Press Ctrl+C to stop.")

try:
    while True:
        # Read temperature and humidity
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN, retries=5, delay_seconds=3)

        if humidity is not None and temperature is not None:
            print(f"Temperature: {temperature:.1f}°C | Humidity: {humidity:.1f}%")
        else:
            print("Failed to retrieve data from the sensor. Retrying...")

        time.sleep(5)  # Allow sensor to reset

except KeyboardInterrupt:
    print("\nProgram stopped by user.")

finally:
    GPIO.cleanup()  # Clean up GPIO settings
    print("Exiting...")
