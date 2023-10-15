import streamlit as st
import pandas as pd
import pydeck as pdk

st.set_page_config(
    page_title="Mapping",
    page_icon="🌍",
)

data = pd.read_csv("DATA.csv", sep=",")
dept = pd.read_csv("dept.csv", sep=",")

merged_data = pd.merge(data, dept, on="dept")

pathology_level = st.selectbox("Select pathology level", ["patho_niv1", "patho_niv2", "patho_niv3"])
pathology = st.selectbox("Select pathology", data[pathology_level].unique())

filtered_data = merged_data[merged_data[pathology_level] == pathology]

occurrence_data = filtered_data.groupby("dept").size().reset_index(name="Occurrence")

colonnes_choisies = ["patho_niv1", "patho_niv2", "patho_niv3", "dept", "Latitude", "Longitude"]

merged_data = merged_data[colonnes_choisies]

layer = pdk.Layer(
    "ScatterplotLayer",
    data=merged_data,
    get_position=["Longitude", "Latitude"],
    get_color="Occurrence",
    get_radius=5000,
    pickable=True,
)

view = pdk.ViewState(latitude=46.2276, longitude=2.2137, zoom=5, pitch=50)

map = pdk.Deck(layers=[layer], initial_view_state=view)

st.pydeck_chart(map)
