import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(
    page_title="Mapping",
    page_icon="🌍",
)

data = pd.read_csv("DATA.csv",sep=",")

st.title("Répartition par région en France")

# Créer un graphique de dispersion interactif avec Plotly Express
fig = px.scatter_geo(data, 
                     locations="region",  # Colonne contenant les codes de région
                     locationmode="ISO-3",  # Mode de localisation (ISO-3 pour les codes de région)
                     title="Répartition par région en France",
                     color="region",  # Utilisez la colonne "region" pour la couleur
                     projection="natural earth"  # Type de projection cartographique
                    )

# Personnaliser le style de la carte (facultatif)
fig.update_geos(
    scope="europe",  # Limiter la carte à la région Europe (pour la France)
    showcoastlines=True,
    coastlinecolor="Black",
    showland=True,
    landcolor="white",
    showocean=True,
    oceancolor="LightBlue",
)

# Afficher la carte
st.plotly_chart(fig)