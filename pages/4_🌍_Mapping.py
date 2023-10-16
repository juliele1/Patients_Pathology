import streamlit as st
import pandas as pd
import pydeck as pdk
from PIL import Image
from streamlit_extras.app_logo import add_logo
from streamlit_extras.colored_header import colored_header
import webbrowser

st.set_page_config(
    page_title="Mapping",
    page_icon="🌍",
)

colored_header(
    label="Mapping",
    color_name="violet-70",
    description="",
)

github_link = "https://github.com/juliele1"
logo_path = 'github.jpeg'
logo = Image.open(logo_path)

st.sidebar.image(logo, width=100)
if st.sidebar.button("Visit my GitHub"):
    webbrowser.open_new_tab(github_link)

linkedin_link = "https://www.linkedin.com/in/julie-chen-/"
logo_path = 'linkd.png'
logo = Image.open(logo_path)

st.sidebar.image(logo, width=70)
if st.sidebar.button("Visit my LinkedIn"):
    webbrowser.open_new_tab(linkedin_link)

st.sidebar.write("#datavz2023efrei")

data = pd.read_csv("DATA.csv", sep=",")
dept = pd.read_csv("dept.csv", sep=",")

st.title("Mapping of the number of patients by department")

niveau_maladie = st.selectbox(
    "Select the level of pathology", data.columns[1:4])

maladies = data[niveau_maladie].unique()
choix_maladie = st.selectbox("Select the pathology", maladies)

filtered_data = data[data[niveau_maladie] == choix_maladie]

merged_data = filtered_data.merge(dept, on='dept')

st.pydeck_chart(pdk.Deck(
    map_style='mapbox://styles/mapbox/dark-v9',
    initial_view_state=pdk.ViewState(
        latitude=46.603354,
        longitude=2.703788,
        zoom=5,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
            'HexagonLayer',
            data=merged_data,
            get_position=['Longitude', 'Latitude'],
            radius=20000,
            elevation_scale=4,
            elevation_range=[0, 1000],
            pickable=True,
            extruded=True,
        ),
    ],
))
