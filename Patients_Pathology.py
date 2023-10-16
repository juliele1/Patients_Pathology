import streamlit as st
from PIL import Image
import webbrowser

st.set_page_config(
    page_title="Patients' Pathology",
    page_icon="🫀",
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

image = Image.open('welcome.jpg')
st.image(image, width=700, caption='Hope you like it !')

st.write("The data provides information on the patient populations covered by all health insurance schemes. It is available by disease, chronic treatment, care episode, gender, age group, region, and department.")
st.write("The population in the mapping encompasses all beneficiaries of mandatory health insurance, regardless of their affiliation scheme: \n\n - Those who have received at least one benefit during the year (such as doctor visits, nursing care, physical therapy, medication, lab tests, transportation, etc.) \n\n - and/or those who have stayed at least once in a public or private healthcare facility during the year (including hospitalizations in medicine, surgery, obstetrics, psychiatry, follow-up care and rehabilitation, outpatient visits, or home hospitalization). \n\n In 2021, this population consisted of 68.7 million beneficiaries from all health insurance schemes who have utilized reimbursed healthcare services. This population is used by the National Health Insurance Fund (Cnam) to conduct numerous studies and generate data on diseases and healthcare expenses.")
