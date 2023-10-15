import streamlit as st
import pandas as pd
import pydeck as pdk
import requests

st.set_page_config(
    page_title="Mapping",
    page_icon="🌍",
)

data = pd.read_csv("DATA.csv",sep=",")

niveau_maladie = st.selectbox("Sélectionner le niveau de maladie", ["patho_niv1", "patho_niv2", "patho_niv3"])

maladies = data[niveau_maladie].unique()
maladie_selectionnee = st.selectbox(f"Sélectionner la maladie ({niveau_maladie})", maladies)

# Filtrer les données en fonction du niveau de maladie et de la maladie sélectionnée
filtered_data = data[data[niveau_maladie] == maladie_selectionnee]

# Regrouper les données par région et compter le nombre d'occurrences
region_counts = filtered_data.groupby("region").size().reset_index()
region_counts.columns = ["region", "occurrences"]

# Fonction pour obtenir les coordonnées géographiques à partir d'une adresse
def get_coordinates(address):
    url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {"address": address, "key": "YOUR_API_KEY"}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        results = response.json()["results"]
        if len(results) > 0:
            location = results[0]["geometry"]["location"]
            return location["lat"], location["lng"]
    return None

# Exemple d'utilisation de la fonction get_coordinates
address = "1600 Amphitheatre Parkway, Mountain View, CA"
coordinates = get_coordinates(address)
if coordinates is not None:
    lat, lng = coordinates
    print(f"Latitude: {lat}, Longitude: {lng}")
else:
    print("Unable to get coordinates for address:", address)


# Afficher la carte avec Pydeck
st.title("Carte des occurrences de maladies par région")
st.pydeck_chart(pdk.Deck(
    initial_view_state=pdk.ViewState(
        latitude=46.603354,
        longitude=1.888334,
        zoom=5,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            "HexagonLayer",
            data=region_counts,
            get_position="[longitude, latitude]",
            radius=100000,
            elevation_scale=5000,
            elevation_range=[0, 3000],
            get_fill_color="[occurrences, occurrences/1000, occurrences/1000, 200]",
            pickable=True,
            extruded=True,
        ),
    ],
))


