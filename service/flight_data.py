class FlightData:
    # This class is responsible for structuring the flight data.
    # data for round trip
    def __init__(self, data: dict):
        self.price = data['price']

        self.id = data['id'].split("|")

        self.origin_city = data['cityFrom']
        self.origin_airport = data['flyFrom']
        self.destination_city = data['cityTo']
        self.destination_airport = data['flyTo']

        self.nights_in_dst = data['nightsInDest']

        length = len(data['route'])

        self.departure_route = [data['route'][i] for i in range(length) if data['route'][i]['return'] == 0]
        self.return_route = [data['route'][i] for i in range(length) if data['route'][i]['return'] == 1]

        self.departure_date = self.departure_route[0]['local_departure'].split("T")[0]
        self.return_date = self.return_route[0]['local_departure'].split("T")[0]

        # check if route has a stopover
        # default length is 2
        self.stop_overs = 0
        if length > 2:
            self.stop_overs = length - 2
            self.via_city = self.departure_route[1]['cityTo']
