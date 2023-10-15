import streamlit as st
import pandas as pd
import missingno as msno
import matplotlib.pyplot as plt
import time

st.set_page_config(
    page_title="Preparation for the dataset",
    page_icon="🧠",
    layout="wide",
)

st.title('Preparation for the dataset of patients pathology')

with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(label="Download complete!", state="complete", expanded=False)

st.button('Rerun')

with st.status("Downloading data...", expanded=True) as status:
    st.write("Searching for data...")
    time.sleep(2)
    st.write("Found URL.")
    time.sleep(1)
    st.write("Downloading data...")
    time.sleep(1)
    status.update(label="Download complete!", state="complete", expanded=False)

st.button('Rerun')

@st.cache_data
def load_data(nrows):
    data = pd.read_csv("effectifs.csv",sep=";")
    data = data[data['annee'] == year_to_filter]
    return data

year_to_filter = 2021

data = load_data(year_to_filter)

st.write("Dataset loaded and filtered successfully!")
st.write("We choose the dataset from 2021 to use more recent data.")
st.write(data)
st.write("We can see some similiaraties with different columns like : cla_age_5 with libelle_classe_age and sexe with libelle_sexe. To be more efficient we will delete cla_age_5 and sexe.")
data = data.drop(columns="cla_age_5")
data = data.drop(columns="sexe")

st.write("Missing bar chart")
fig1 = plt.figure(figsize=(8, 6))
msno.bar(data)
st.pyplot(fig1)

st.write("Percentage of missing values ​​per column:")
missing_percentage = data.isnull().mean() * 100

missing_percentage_df = pd.DataFrame({'Colomns': missing_percentage.index, 'Percentage of missing values ​​per column': missing_percentage.values})

st.dataframe(missing_percentage_df, width=500)

st.write("We can see that there are missing data, we have to delete the lines of the missing data of the columns : top, patho_niv1, ntop, prev. We decided to delete those lines because we can't replace the missing values with another value.")

data = data.dropna(subset=["top"])

data = data.dropna(subset=["patho_niv1"])

data = data.dropna(subset=["ntop"])

data = data.dropna(subset=["prev"])

st.write("Missing bar chart")

fig2 = plt.figure(figsize=(8, 6))
msno.bar(data)
st.pyplot(fig2)

st.write("Percentage of missing values ​​per column:")
missing_percentage = data.isnull().mean() * 100
missing_percentage_df = pd.DataFrame({'Colomns': missing_percentage.index, 'Percentage of missing values ​​per column': missing_percentage.values})
st.dataframe(missing_percentage_df, width=500)

st.write("There is a possibility that the disease doesn't have a sub-category disease, we will fullfil the remainded missing values with Pas de pathologie.")

data["patho_niv2"] = data["patho_niv2"].fillna("Pas de pathologie")
data["patho_niv3"] = data["patho_niv3"].fillna("Pas de pathologie")

st.write("Missing bar chart")

fig3 = plt.figure(figsize=(8, 6))
msno.bar(data)
st.pyplot(fig3)

st.write("Percentage of missing values ​​per column:")
missing_percentage = data.isnull().mean() * 100
missing_percentage_df = pd.DataFrame({'Colomns': missing_percentage.index, 'Percentage of missing values ​​per column': missing_percentage.values})
st.dataframe(missing_percentage_df, width=500)

st.write("Information on the dataframe :")
info_df = pd.DataFrame({
    "Columns": data.columns,
    "Type": [str(data[col].dtype) for col in data.columns]
})

st.dataframe(info_df, width=600)

st.write("Dataframe's descriptive statistics :")
st.write(data.describe())

st.write("We can see that we have object type values. We have to change their type into category type to be able to use them in our analysis.")

data['patho_niv1'] = data['patho_niv1'].astype('category')
data['patho_niv2'] = data['patho_niv2'].astype('category')
data['patho_niv3'] = data['patho_niv3'].astype('category')
data['top'] = data['top'].astype('category')
data['dept'] = data['dept'].astype('category')
data['niveau_prioritaire'] = data['niveau_prioritaire'].astype('category')
data['libelle_classe_age'] = data['libelle_classe_age'].astype('category')
data['libelle_sexe'] = data['libelle_sexe'].astype('category')

st.write("Information on the dataframe :")
info_df = pd.DataFrame({
    "Columns": data.columns,
    "Type": [str(data[col].dtype) for col in data.columns]
})

st.dataframe(info_df, width=600)

st.write(data.head())
st.write(data.tail())
st.write(data)