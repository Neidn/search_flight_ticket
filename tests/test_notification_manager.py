######################################################################
#  N O T I F I C A T I O N   M A N A G E R   T E S T   C A S E S
######################################################################
# pylint: disable=too-many-public-methods
import unittest
from unittest import mock

from .factories import FlightDataFactory
from service.notification_manager import NotificationManager


class TestNotificationManager(unittest.TestCase):
    """Test Cases for Notification Manager"""

    @classmethod
    def setUpClass(cls):
        """This runs once before the entire test suite"""
        cls.notification_manager = NotificationManager()
        pass

    @classmethod
    def tearDownClass(cls):
        """This runs once after the entire test suite"""
        pass

    def setUp(self):
        """This runs before each test"""
        pass

    def tearDown(self):
        """This runs after each test"""
        pass

    ######################################################################
    #  T E S T   C A S E S
    ######################################################################

    def test_send_sms(self):
        """Test send_sms method"""
        """
        message = "Test Message"
        target_phone_number = "+1234567890"
        with mock.patch('service.data_manager.Client') as mock_client:
            mock_message = mock.MagicMock()
            mock_message.sid = "TestSid"
            mock_client.return_value.messages.create.return_value = mock_message
            response = self.notification_manager.send_sms(message, target_phone_number)
            self.assertTrue(response)
            mock_client.return_value.messages.create.assert_called_once_with(
                body=message,
                from_=self.data_manager.twilio_phone_number,
                to=target_phone_number
            )
        """
        pass
