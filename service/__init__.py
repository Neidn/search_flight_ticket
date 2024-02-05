# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import os

from dotenv import load_dotenv

from .main import main

load_dotenv(verbose=True)

main()
