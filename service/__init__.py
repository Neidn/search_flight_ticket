# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from pprint import pprint
from dotenv import load_dotenv

load_dotenv(verbose=True)

from .data_manager import DataManager
from .flight_search import FlightSearch

data_manager = DataManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_data()

for i in range(len(sheet_data)):
    sheet_data[i]['iataCode'] = flight_search.get_iata_code(sheet_data[i]['city'])

    data_manager.update_iata_code(sheet_data[i]['id'], sheet_data[i]['iataCode'])

pprint(sheet_data)
