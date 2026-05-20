from geopy.geocoders import Nominatim
import time

def reverse_geocode_coordinates(coordinates_list):
    """
    Führt Reverse Geocoding für eine Liste oder pandas Series von Koordinaten durch.

    Parameter:
    coordinates_list : Liste oder pandas Series von Strings im Format "lat, lon"

    Rückgabe:
    Liste mit Ländernamen
    """
    geolocator = Nominatim(user_agent="wildfire_project_dmoinqi_20260520_1", timeout=10)
    #timeout = 10, falls der Server nicht reagiert, damit de Code nicht hängen bleibt

    adresses = []

    for i in coordinates_list:
        loc = geolocator.reverse(i) #es wird reverse geocoding verwendet, heisst von den Koordinaten zum Ort

        if loc:
            adresses.append(loc.address) #wenn eine Adresse gefunden wird, wird die der Liste "adresses" angehängt
        else:
            adresses.append("Unbekannt") #wenn keine Adresse gefunden wird, wir "Unbekannt" der Liste angehängt

        time.sleep(1)  #Pause --> wichtig wegen API-Regeln

    return adresses
