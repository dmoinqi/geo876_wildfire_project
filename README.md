# Globale Wildfire-Analyse

## Projektbeschreibung
Das Projekt analysiert globale Wildfires anhand satellitenbasierter Daten des NASA FIRMS Systems. Der Fokus liegt auf der Untersuchung der räumlichen Verteilung, der Intensität und Detektionssicherheit von Wildfires innerhalb eines kurzen Zeitraums (letzte 24 Stunden). Der Datensatz liegt im `.csv`-Format vor (abgerufen am 19.05.2026) und enthält georeferenzierte Punktdaten, wobei jede Zeile ein detektiertes Wildfire repräsentiert. Wichtige Variablen wie die geografische Lage (Latitude/Longitude), die Detektionssicherheit (confidence) sowie die Feuerintensität (Fire Radiative Power, FRP) werden genutzt, um die Verteilung und Eigenschaften der Brände zu analysieren.

## Zielsetzung
Das Ziel dieses Projekts ist es, eine automatisierte Pipeline zu entwickeln, die Wildfires verarbeitet, relevante Informationen herausfiltert, eine gezielte Analyse ermöglicht und die Ergebnisse übersichtlich auf einer interaktiven Karte visualisiert.

## Datenquellen
* **NASA FIRMS (Fire Information for Resource Management System): _VIIRS 375m / S-NPP (24h)_**  
  https://firms.modaps.eosdis.nasa.gov/active_fire/  
  _(abgerufen: 19.05.2026)_

* *Hinweis: Die verwendeten Rohdaten sind bereits im Repository im Ordner `data/raw/` enthalten und müssen nicht separat heruntergeladen werden.*

## Reproduzierbare Umgebung
1. Stelle sicher, dass Conda installiert ist.
2. Erstelle die Umgebung: `conda env create -f environment.yml`
3. Aktiviere: `conda activate sds-env`

## Ausführung 
Das gesamte Projekt ist im Jupyter Notebook `wildfire_mapping.ipynb` umgesetzt.
Führe das Jupyter Notebook `wildfire_mapping.ipynb` von oben bis unten aus. Das Histogramm und die interaktive Karte werden zusätzlich in den Ordner `outputs` exportiert. 

## Projektstruktur 
Die Projektstruktur gestaltet sich wie folgt: 

- **geo876_wildfire_project/**
  - **data/**
    - **processed/** – Bereinigte und verarbeitete Daten (CSV, GeoPackage)
    - **raw/** – Rohdaten (Originaldatensatz von NASA FIRMS)

  - **notebooks/**
    - **wildfire_mapping.html** – `.html` Ausdruck der ausgeführten Jupyter Notebooks 
    - **wildfire_mapping.ipynb** – zentrales Jupyter Notebook für Analyse und Visualisierung

  - **outputs/**
    - **histogram_fire_intensity.png** – Histogramm der Feuerintensität
    - **wildfire_map.html** – Interaktive Karte

  - **scripts/**
    - **classification.py** – beinhaltet Funktion für Klassifikation der Brandintensität
    - **spatial_tools.py** – beinhaltet Funktion für Reverse Geocoding
  
  - **.gitignore** - Liste von Dateien, die nicht synchronisiert werden sollen 
  - **environment.yml** – Definition der Python-Umgebung  
  - **README.md** – Projektbeschreibung  


