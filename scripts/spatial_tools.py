from geopy.geocoders import Nominatim
import time
from tqdm import tqdm

def reverse_geocode_coordinates(coordinates_list):
    """
    Führt Reverse Geocoding für eine Liste oder pandas Series von Koordinaten durch.

    Parameter:
    coordinates_list : Liste oder pandas Series von Strings im Format "lat, lon"

    Rückgabe:
    Liste mit Ländernamen
    """
    geolocator = Nominatim(user_agent="wildfire_project_dmoinqi_20260520_1", timeout=10)

    adresses = []

    for i in tqdm(coordinates_list):
        loc = geolocator.reverse(i)

        if loc:
            adresses.append(loc.address)
        else:
            adresses.append("Unbekannt")

        time.sleep(1)  #Pause --> wichtig wegen API-Regeln


    return adresses
