from pprint import pprint
import os

from .data_manager import DataManager
from .flight_search import FlightSearch
from .flight_data import FlightData
from .notification_manager import NotificationManager
from .user_data import UserData


def main():
    departure_city_iata = os.getenv("DEPARTURE_CITY_IATA")
    data_manager = DataManager()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()
    user_data = UserData(os.getenv('USER_DATABASE_NAME'))
    user_list = user_data.query_all_user()

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
            # notification_manager.send_sms(msg, '+1234567890')

            # if route has a stopover, show msg with stopover city
            if flight_data.stop_overs > 0:
                msg += "\n"
                msg += f"Flight has {flight_data.stop_overs} stop over, via {flight_data.via_city}."

            for user in user_list:
                notification_manager.send_email(msg, user['email'])
