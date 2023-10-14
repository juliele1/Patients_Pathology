import streamlit as st
from PIL import Image


st.set_page_config(
    page_title="Patients' Pathology",
    page_icon="🫀",
)

st.write("Welcome to my page where I show you what my dataset is about !")

image = Image.open('welcome.jpg')
st.image(image, width=700,caption='Hope you like it !')

st.write("The data provides information on the patient populations covered by all health insurance schemes. It is available by disease, chronic treatment, care episode, gender, age group, region, and department.")
st.write("The population in the mapping encompasses all beneficiaries of mandatory health insurance, regardless of their affiliation scheme: \n\n - Those who have received at least one benefit during the year (such as doctor visits, nursing care, physical therapy, medication, lab tests, transportation, etc.) \n\n - and/or those who have stayed at least once in a public or private healthcare facility during the year (including hospitalizations in medicine, surgery, obstetrics, psychiatry, follow-up care and rehabilitation, outpatient visits, or home hospitalization). \n\n In 2021, this population consisted of 68.7 million beneficiaries from all health insurance schemes who have utilized reimbursed healthcare services. This population is used by the National Health Insurance Fund (Cnam) to conduct numerous studies and generate data on diseases and healthcare expenses.")