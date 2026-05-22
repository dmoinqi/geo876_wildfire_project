from geopy.geocoders import Nominatim #kostenloser geocoding service von OpenStreetMap
import time

def reverse_geocode_coordinates(coordinates_list):
    """
    Führt Reverse Geocoding für eine Liste oder pandas Series von Koordinaten durch.

    Für jede Koordinate im Format "lat, lon" wird mithilfe des Nominatim-Geocoders
    eine Adresse ermittelt. Die Funktion wird insbesondere verwendet, um die
    räumliche Verteilung von Brandereignissen (z. B. Länderzuordnung) zu analysieren.

    Parameter
    ----------
    coordinates_list : list oder pandas.Series
        Liste oder Series von Strings im Format "latitude, longitude".

    Returns
    -------
    list
        Liste von Adressen (Strings). Falls keine Adresse gefunden wird,
        wird "Unbekannt" zurückgegeben.

    Hinweise
    --------
    - Es wird eine Pause von 1 Sekunde zwischen den Anfragen eingefügt,
      um die API-Nutzungsregeln von Nominatim einzuhalten, da geopy im Hintergrund
      eine WebAPI verwendet.
    """
    geolocator = Nominatim(user_agent="wildfire_project_dmoinqi_20260520_1") #benutzerdefinierter Name, damit OSM weiss, wer die Anfrage stellt

    adresses = [] #leere List, der mit dem for-Loop Adressen hinzugefügt werden

    for i in coordinates_list:
        loc = geolocator.reverse(i) #es wird reverse geocoding verwendet, heisst von den Koordinaten zum Ort

        if loc:
            adresses.append(loc.address) #wenn eine Adresse gefunden wird, wird die der Liste "adresses" angehängt
        else:
            adresses.append("Unbekannt") #wenn keine Adresse gefunden wird, wird "Unbekannt" der Liste angehängt

        time.sleep(1)  #Pause --> wichtig wegen API-Regeln

    return adresses

