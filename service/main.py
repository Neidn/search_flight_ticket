from pprint import pprint
import os

from .data_manager import DataManager
from .flight_search import FlightSearch
from .flight_data import FlightData


def main():
    departure_city_iata = os.getenv("DEPARTURE_CITY_IATA")
    data_manager = DataManager()
    flight_search = FlightSearch()

    sheet_data = data_manager.get_data()

    for i in range(len(sheet_data)):
        if not sheet_data[i]['iataCode']:
            sheet_data[i]['iataCode'] = flight_search.get_iata_code(sheet_data[i]['city'])
            data_manager.update_iata_code(sheet_data[i]['id'], sheet_data[i]['iataCode'])

        data = flight_search.get_flight_data(departure_city_iata, sheet_data[i]['iataCode'])
        if not data:
            continue
        flight_data = FlightData(data)

        if flight_data.price < sheet_data[i]['lowestPrice']:
            msg = f"Low price alert! Only ${flight_data.price} to fly from {flight_data.origin_city}-{flight_data.origin_airport} to {flight_data.destination_city}-{flight_data.destination_airport}, from {flight_data.departure_date} to {flight_data.return_date}."
            print(msg)
            # data_manager.send_sms(msg)
