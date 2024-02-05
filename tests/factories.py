import factory
from factory.fuzzy import FuzzyDecimal
from service.flight_data import FlightData


class FlightDataFactory(factory.Factory):
    """Creates Flight Data for testing"""

    class Meta:
        """Maps factory to data model"""

        model = FlightData

    price = FuzzyDecimal(10, 1000)
    origin_city = factory.Faker("city")
    origin_airport = factory.Faker("airport")
    destination_city = factory.Faker("city")
    destination_airport = factory.Faker("airport")
    nights_in_dst = FuzzyDecimal(2, 28)

    departure_date = factory.Faker("date")
    return_date = factory.Faker("date")

    departure_route = [
        {
            "local_departure": departure_date,
            "return": 0
        }
    ]

    return_route = [
        {
            "local_departure": return_date,
            "return": 1
        }
    ]
