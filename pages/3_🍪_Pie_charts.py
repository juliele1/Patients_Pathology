import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Distribution",
    page_icon="🍪",
)

data = pd.read_csv("DATA.csv",sep=",")

import pyecharts.options as opts
from pyecharts.charts import Pie

st.title("Distribution by age group")

libelle_classe_age_counts = data["libelle_classe_age"].value_counts().reset_index()
libelle_classe_age_counts.columns = ["Age class", "Number of occurrences"]


pie = (
    Pie()
    .add(
        "",
        [list(z) for z in zip(libelle_classe_age_counts["Age class"], libelle_classe_age_counts["Number of occurrences"])],
        radius=["40%", "75%"],
        center=["50%", "50%"],
        rosetype="radius",
        label_opts=opts.LabelOpts(is_show=False),
    )
    .set_global_opts(title_opts=opts.TitleOpts(title="Distribution by age group"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c} ({d}%)"))
)

pie_html = pie.render_embed()

import streamlit.components.v1 as stc

stc.html(pie_html)

st.write("We can think that we have a homogeneous distribution of patients by age group but the distribution is mostly between different old age groups. Indeed, there is 55,61% of old people, 19.74% of middle age people, 7.74% of young adults and 10.55% of children and teeanagers. We can deduct that most people coming to the hospital are old people.")

st.title("Distribution by sexe")

libelle_sexe_counts = data["libelle_sexe"].value_counts().reset_index()
libelle_sexe_counts.columns = ["Sexe", "Number of occurrences"]

fig = px.pie(libelle_sexe_counts, names="Sexe", values="Number of occurrences",
             title="Distribution by sexe")

st.plotly_chart(fig)

st.write("We can see that the male and female quota is balanced.")

st.title("Distribution by priority level")

niveau_prioritaire_counts = data["niveau_prioritaire"].value_counts().reset_index()
niveau_prioritaire_counts.columns = ["Priority level", "Number of occurrences"]

fig = px.pie(niveau_prioritaire_counts, names="Priority level", values="Number of occurrences",
             title="Distribution by priority level")

st.plotly_chart(fig)

st.write("We can see that most patients have a high priority level, mostly 2 and 3, 3 being the highiest value. Indeed, 73.1% of patients have 2-3 priority level compared to 16.6% of patients that have 1 priority level. It means that patients come to the hospital essentially when they are in a critical state.")

