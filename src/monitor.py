import RPi.GPIO as GPIO
import time
import logging
import requests
import atexit

# ==============================
# Configuration
# ==============================
LOG_FILE = "/var/log/vibration_monitor.log"
VIBRATION_SENSOR_PIN = 14  # Adjust based on wiring
ALERT_WEBHOOK = "https://example.com/alert"  # Replace with actual endpoint
CHECK_INTERVAL = 0.1  # Seconds between sensor checks
ALERT_RETRIES = 3     # Number of times to retry sending an alert

# ==============================
# Logging setup
# ==============================
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# ==============================
# GPIO setup
# ==============================
GPIO.setmode(GPIO.BCM)
GPIO.setup(VIBRATION_SENSOR_PIN, GPIO.IN)

# ==============================
# Functions
# ==============================
def send_alert():
    """Send an alert to a remote server or dashboard with retries."""
    for attempt in range(1, ALERT_RETRIES + 1):
        try:
            response = requests.post(ALERT_WEBHOOK, json={"message": "Vibration detected!"}, timeout=5)
            if response.status_code == 200:
                logging.info("Alert successfully sent to server.")
                return True
            else:
                logging.warning(f"Attempt {attempt}: Failed to send alert, status code: {response.status_code}")
        except requests.RequestException as e:
            logging.error(f"Attempt {attempt}: Error sending alert: {e}")
        time.sleep(1)  # wait before retrying
    return False


def monitor_vibrations():
    """Continuously monitor for vibrations and trigger alerts."""
    logging.info("Vibration monitoring started.")
    print("Monitoring vibrations... Press Ctrl+C to stop.")

    try:
        while True:
            if GPIO.input(VIBRATION_SENSOR_PIN) == GPIO.HIGH:
                logging.warning("Vibration detected!")
                print("Vibration detected!")
                send_alert()
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        logging.info("Vibration monitoring stopped by user.")
        print("\nStopping vibration monitoring.")
    except Exception as e:
        logging.error(f"Unexpected error in monitoring loop: {e}")


def cleanup():
    """Cleanup GPIO on exit."""
    GPIO.cleanup()
    logging.info("GPIO cleaned up successfully.")


# ==============================
# Main Execution
# ==============================
if __name__ == "__main__":
    atexit.register(cleanup)
    monitor_vibrations()
