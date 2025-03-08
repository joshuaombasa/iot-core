import unittest
from src.monitor import send_alert

class TestVibrationMonitor(unittest.TestCase):
    def test_send_alert(self):
        result = send_alert()
        self.assertIsNone(result)  # Ensure function runs without error

if __name__ == "__main__":
    unittest.main()
