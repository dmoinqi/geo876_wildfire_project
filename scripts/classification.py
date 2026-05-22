def classify_fire_intensity(frp):
    """
        Klassifiziert die Feuerintensität basierend auf der Fire Radiative Power (FRP).

        Die Funktion teilt kontinuierliche FRP-Werte (in Megawatt) in diskrete
        Intensitätsklassen ein. Diese Klassen werden anschliessend für die
        farbliche Darstellung der Brandereignisse in der interaktiven Karte verwendet.

        Die Klassengrenzen wurden nach den typischen Feuerintensitäten gemäss ArcGIS Fire
        Radiative Power Erklärung eingefärbt:
        https://experience.arcgis.com/experience/a0dcc4b8e8ab49b58a520f5acb983345/page/FIRE

        Parameter
        ----------
        frp : float
            Fire Radiative Power eines Brandereignisses in Megawatt (MW).

        Returns
        -------
        str : string
            Eine kategorische Intensitätsklasse:
            - "sehr niedrig (<10 MW)"
            - "niedrig (10-99 MW)"
            - "mittel (100-299 MW)"
            - "hoch (300-749 MW)"
            - "extrem (>= 750 MW)"
        """
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