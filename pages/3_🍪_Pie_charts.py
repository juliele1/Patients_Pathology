import streamlit as st
import pandas as pd
from streamlit_echarts import st_pyecharts
import pyecharts.options as opts
from pyecharts.charts import Pie

st.set_page_config(
    page_title="Distribution",
    page_icon="🍪",
)

data = pd.read_csv("DATA.csv",sep=",")

selected_chart = st.selectbox("Select a graph", ["Age group", "Sexe", "Priority level"])

if selected_chart == "Age group":
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
            label_opts=opts.LabelOpts(formatter="{b}: {d}%"),
        )
        .set_global_opts(title_opts=opts.TitleOpts(title="Distribution by age group"), 
                        legend_opts=opts.LegendOpts(is_show=False))
    )

    st_pyecharts(pie, height='500px')

    st.write("We can think that we have a homogeneous distribution of patients by age group but the distribution is mostly between different old age groups. Indeed, there is 55,61% of old people, 19.74% of middle age people, 7.74% of young adults and 10.55% of children and teeanagers. We can deduct that most people coming to health care are old people.")

if selected_chart == "Sexe":
    st.title("Distribution by sexe")

    libelle_sexe_counts = data["libelle_sexe"].value_counts().reset_index()
    libelle_sexe_counts.columns = ["Sexe", "Number of occurrences"]

    pie = (
        Pie()
        .add("", [list(z) for z in zip(libelle_sexe_counts["Sexe"], libelle_sexe_counts["Number of occurrences"])])
        .set_global_opts(title_opts=opts.TitleOpts(title="Distribution by sexe"), legend_opts=opts.LegendOpts(is_show=True, pos_left="right", orient="vertical"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    )

    st_pyecharts(pie, height='500px')

    st.write("We can see that the male and female quota is balanced.")

if selected_chart == "Priority level":
    st.title("Distribution by priority level")

    niveau_prioritaire_counts = data["niveau_prioritaire"].value_counts().reset_index()
    niveau_prioritaire_counts.columns = ["Priority level", "Number of occurrences"]

    pie = (
        Pie()
        .add("", [list(z) for z in zip(niveau_prioritaire_counts["Priority level"], niveau_prioritaire_counts["Number of occurrences"])])
        .set_global_opts(title_opts=opts.TitleOpts(title="Distribution by priority level"),legend_opts=opts.LegendOpts(is_show=True, pos_left="right", orient="vertical"))
        .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
    )

    st_pyecharts(pie, height='500px')

    st.write("We can see that most patients have a high priority level, mostly 2 and 3, 3 being the highiest value. Indeed, 73.1% of patients have 2-3 priority level compared to 16.6% of patients that have 1 priority level. It means that patients see a doctor essentially when they are in a critical state.")



