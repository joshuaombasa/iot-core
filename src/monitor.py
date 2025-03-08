import RPi.GPIO as GPIO
import time
import logging
import requests

# Configure logging for production use
logging.basicConfig(filename='/var/log/vibration_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Define the GPIO pin connected to the vibration sensor
VIBRATION_SENSOR_PIN = 14  # Change according to your wiring
ALERT_WEBHOOK = "https://example.com/alert"  # Replace with actual endpoint

# Set up GPIO mode
GPIO.setmode(GPIO.BCM)
GPIO.setup(VIBRATION_SENSOR_PIN, GPIO.IN)

def send_alert():
    """Send an alert to a remote server or dashboard."""
    try:
        response = requests.post(ALERT_WEBHOOK, json={"message": "Vibration detected!"})
        if response.status_code == 200:
            logging.info("Alert successfully sent to server.")
        else:
            logging.warning(f"Failed to send alert, status code: {response.status_code}")
    except Exception as e:
        logging.error(f"Error sending alert: {e}")

def monitor_vibrations():
    logging.info("Vibration monitoring started.")
    print("Monitoring vibrations... Press Ctrl+C to stop.")
    try:
        while True:
            if GPIO.input(VIBRATION_SENSOR_PIN) == GPIO.HIGH:
                logging.warning("Vibration detected!")
                print("Vibration detected!")
                send_alert()
            time.sleep(0.1)  # Adjust as needed
    except KeyboardInterrupt:
        logging.info("Vibration monitoring stopped by user.")
        print("\nStopping vibration monitoring.")
        GPIO.cleanup()
    except Exception as e:
        logging.error(f"Unexpected error: {e}")
        GPIO.cleanup()

if __name__ == "__main__":
    monitor_vibrations()
