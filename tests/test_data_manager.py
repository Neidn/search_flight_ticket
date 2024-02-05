######################################################################
#  D A T A   M A N A G E R   T E S T   C A S E S
######################################################################
# pylint: disable=too-many-public-methods
import unittest
from unittest import mock

import random
from service.data_manager import DataManager


class TestDataManager(unittest.TestCase):
    """Test Cases for Data Manager"""

    @classmethod
    def setUpClass(cls):
        """This runs once before the entire test suite"""
        cls.data_manager = DataManager()
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
    def test_get_data(self):
        """Test get_data method"""
        data = self.data_manager.get_data()
        self.assertIsInstance(data, list)
        self.assertTrue(len(data) > 0)

    def test_update_iata_code(self):
        """Test update_iata_code method"""
        data = self.data_manager.get_data()

        random_index = random.randint(0, len(data) - 1)

        row_id = data[random_index]['id']
        test_case = data[random_index]
        before_iata_code = test_case['iataCode']
        new_iata_code = "TEST"
        response = self.data_manager.update_iata_code(row_id, new_iata_code)
        self.assertIsInstance(response, dict)
        self.assertEqual(response['price']['id'], row_id)

        # Rollback
        response = self.data_manager.update_iata_code(row_id, before_iata_code)
        self.assertIsInstance(response, dict)
        self.assertEqual(response['price']['id'], row_id)
