import unittest
from unittest.mock import patch
from src.monitor import send_alert

class TestVibrationMonitor(unittest.TestCase):

    @patch("src.monitor.alert_service.send")  # Mock the alert service
    def test_send_alert(self, mock_send):
        """Test that send_alert calls the alert service correctly."""
        mock_send.return_value = True  # Simulate a successful alert

        result = send_alert()

        mock_send.assert_called_once()  # Ensure the alert service was called
        self.assertTrue(result)  # Validate expected return value

if __name__ == "__main
