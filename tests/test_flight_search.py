######################################################################
#  F L I G H T   S E A R C H   T E S T   C A S E S
######################################################################
# pylint: disable=too-many-public-methods
import unittest
from unittest import mock

from .factories import FlightDataFactory
from service.flight_search import FlightSearch


class TestFlightSearch(unittest.TestCase):
    """Test Cases for Flight Search"""

    @classmethod
    def setUpClass(cls):
        """This runs once before the entire test suite"""
        cls.flight_search = FlightSearch()
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
    def test_get_iata_code(self):
        """Test get_iata_code method"""
        iata_code = self.flight_search.get_iata_code("Paris")
        self.assertIsInstance(iata_code, str)
        self.assertTrue(len(iata_code) > 0)

    def test_get_flight_data(self):
        """Test get_flight_data method"""
        data = self.flight_search.get_flight_data("LON", "PAR")
        self.assertIsInstance(data, dict)
        self.assertTrue(len(data) > 0)
        self.assertIsInstance(data['price'], int)
        self.assertIsInstance(data['id'], str)
        self.assertIsInstance(data['cityFrom'], str)
        self.assertIsInstance(data['flyFrom'], str)
        self.assertIsInstance(data['cityTo'], str)
        self.assertIsInstance(data['flyTo'], str)
        self.assertIsInstance(data['nightsInDest'], int)
        self.assertTrue(data['nightsInDest'] > 0)
        self.assertIsInstance(data['route'], list)
        self.assertTrue(len(data['route']) > 0)
        self.assertIsInstance(data['route'][0], dict)
