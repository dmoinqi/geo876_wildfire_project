#eigene Klassifikationsklasse für die Darstellung der Feuerintensitäten auf der interaktiven Karte
#basierend auf den üblichen Feuerintensitäten gem. https://experience.arcgis.com/experience/a0dcc4b8e8ab49b58a520f5acb983345/page/FIRE
def classify_fire_intensity(frp):
    if frp < 10:
        return "sehr niedrig (<10 MW)"
    elif frp < 100:
        return "niedrig (10-99 MW)"
    elif frp < 300:
        return "mittel (100-299 MW)"
    elif frp < 750:
        return "hoch (300-749 MW)"
    else:
        return "extrem (>= 750 MW)"