import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Patients' Pathology",
    page_icon="🫀",
)

st.write("Welcome to my page where I show you what my dataset is about !")

image = Image.open('welcome.jpg')
st.image(image, width=700,caption='Hope you like it !')


