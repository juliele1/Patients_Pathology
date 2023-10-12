import streamlit as st
import pandas as pd
import plotly.express as px

from math import pi
from bokeh.palettes import Category20c
from bokeh.plotting import figure, show
from bokeh.transform import cumsum

st.set_page_config(
    page_title="Plotting",
    page_icon="📊",
)

data = pd.read_csv("DATA.csv",sep=",")


st.title("Number of occurrences of each disease in patho_niv1")

patho_niv1_counts = data["patho_niv1"].value_counts().reset_index()
patho_niv1_counts.columns = ["Disease", "Number of occurrences"]

patho_niv1_counts = patho_niv1_counts.sort_values(by="Number of occurrences", ascending=False)

fig = px.bar(patho_niv1_counts, x="Number of occurrences", y="Disease", orientation='h', 
             title="Number of occurrences of each disease in patho_niv1",
             labels={"Number of occurrences": "Number of occurrences", "Disease": "Disease"})

fig.update_traces(marker_color="rgba(50, 171, 96, 0.6)")

st.plotly_chart(fig)

st.write("Most patients have a disease in the circulatory system with 83.278 patients, cancer with 70.055 patients or an inflammatory or rare disease or HIV or AIDS with 60.333 patients. We can see that everyone has a disease.")

st.title("Number of occurrences of each disease in patho_niv2")

patho_niv1_counts = data["patho_niv2"].value_counts().reset_index()
patho_niv1_counts.columns = ["Disease", "Number of occurrences"]

patho_niv1_counts = patho_niv1_counts.sort_values(by="Number of occurrences", ascending=False)

fig = px.bar(patho_niv1_counts, x="Number of occurrences", y="Disease", orientation='h', 
             title="Number of occurrences of each disease in patho_niv2",
             labels={"Number of occurrences": "Number of occurrences", "Disease": "Disease"})

fig.update_traces(marker_color="rgba(184, 15, 194, 0.8)")

st.plotly_chart(fig)

st.write("For this graph, we can see that most of the patients don't have a sub-category disease. Indeed, there are 70.144 patients that don't have a sub-category disease. Nonetheless, patients mostly have a sub-category disease even if the number has decreased by two. For example, we have chronic inflammatory disease with 30.249 patients and 20.44 patients that have others cancers as a sub-category disease.")

st.title("Number of occurrences of each disease in patho_niv3")

patho_niv1_counts = data["patho_niv3"].value_counts().reset_index()
patho_niv1_counts.columns = ["Disease", "Number of occurrences"]

patho_niv1_counts = patho_niv1_counts.sort_values(by="Number of occurrences", ascending=False)

fig = px.bar(patho_niv1_counts, x="Number of occurrences", y="Disease", orientation='h', 
             title="Number of occurrences of each disease in patho_niv3",
             labels={"Number of occurrences": "Number of occurrences", "Disease": "Disease"})

fig.update_traces(marker_color="rgba(49, 208, 235, 0.8)")

st.plotly_chart(fig)

st.write("For this graph, we also see that most of the patients don't have a second sub-category disease, even more than the previous graph. Indeed, 123.844 patients don't have a second sub-category disease. However, there are some patients that do have a disease but the number is not very significant compared to our previous graphs. For instance, most patients have other long-term infection with 7558 patients and 7548 patients for occasional hospitalizations.")

st.title("Number of occurrences of each disease in patho_niv1")

# Comptez les occurrences de chaque maladie dans 'patho_niv1'
patho_niv1_counts = data["patho_niv1"].value_counts().reset_index()
patho_niv1_counts.columns = ["Disease", "Number of occurrences"]

# Triez les données par le nombre d'occurrences décroissant
patho_niv1_counts = patho_niv1_counts.sort_values(by="Number of occurrences", ascending=False)

# Créez un graphique à barres horizontal avec Bokeh
p = figure(y_range=patho_niv1_counts["Disease"], plot_height=400, plot_width=600,
           title="Number of occurrences of each disease in patho_niv1",
           toolbar_location=None, tools="")

p.hbar(y="Disease", right="Number of occurrences", height=0.8, source=patho_niv1_counts,
       color="orange", legend_field="Disease")

p.ygrid.grid_line_color = None
p.xaxis.axis_label = "Number of occurrences"
p.yaxis.axis_label = "Disease"

# Affichez le graphique Bokeh dans Streamlit
st.bokeh_chart(p)