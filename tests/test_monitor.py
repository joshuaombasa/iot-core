import unittest
from unittest.mock import patch
from src.monitor import send_alert


class TestVibrationMonitor(unittest.TestCase):
    """Unit tests for the vibration monitoring alert system."""

    @patch("src.monitor.alert_service.send")  # Mock the alert service dependency
    def test_send_alert_success(self, mock_send):
        """Test that send_alert calls the alert service and returns True on success."""
        mock_send.return_value = True  # Simulate successful alert

        result = send_alert()

        mock_send.assert_called_once_with()  # Ensure it was called without arguments
        self.assertTrue(result)

    @patch("src.monitor.alert_service.send")
    def test_send_alert_failure(self, mock_send):
        """Test that send_alert handles failure from the alert service."""
        mock_send.return_value = False  # Simulate failed alert

        result = send_alert()

        mock_send.assert_called_once_with()
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
