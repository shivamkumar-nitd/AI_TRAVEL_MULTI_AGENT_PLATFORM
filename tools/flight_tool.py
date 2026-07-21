import os
import requests
from dotenv import  load_dotenv

load_dotenv()

AVIATIONSTACK_API_KEY = os.getenv("AVIATIONSTACK_API_KEY")

def search_flights(query):
    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": AVIATIONSTACK_API_KEY,
        "limit": 5
    }

    response = requests.get(url, params=params)
    data = response.json()

    flights = []

    if "data" in data:
        for flight in data["data"][:5]:
            airline = flight.get("airline" , {}).get("name" , "N/A")
            departure = flight.get("departure" , {}).get("airport" , "N/A ")
            arrival = flight.get("arrival" , {}).get("airport" , "N/A")

            status = flight.get("flight_status" , "N/A")

            flights.append(f"""Airline: {airline}, Departure: {departure}, Arrival: {arrival}, Status: {status}""")

    return "\n".join(flights)


 