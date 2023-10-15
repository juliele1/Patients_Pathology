import streamlit as st
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, HoverTool
import plotly.express as px
import altair as alt
from bokeh.transform import linear_cmap
from bokeh.models import HoverTool

st.set_page_config(
    page_title="Plotting",
    page_icon="📊",
    layout="wide",
)

data = pd.read_csv("DATA.csv",sep=",")

selected_chart = st.selectbox("Select a graph", ["Patho_niv1", "Patho_niv2", "Patho_niv3"])

if selected_chart == "Patho_niv1":
    st.title("Number of occurrences of each disease in patho_niv1")

    patho_niv1_counts = data["patho_niv1"].value_counts().reset_index()
    patho_niv1_counts.columns = ["Disease", "Number of occurrences"]

    patho_niv1_counts = patho_niv1_counts.sort_values(by="Number of occurrences", ascending=False)

    source = ColumnDataSource(patho_niv1_counts)

    hover = HoverTool(
        tooltips=[
            ("Disease", "@Disease"),
            ("Number of occurrences", "@{Number of occurrences}")
        ]
    )

    color_mapper = linear_cmap(field_name='Number of occurrences', palette="Viridis256", low=patho_niv1_counts["Number of occurrences"].min(), high=patho_niv1_counts["Number of occurrences"].max())

    p = figure(y_range=patho_niv1_counts["Disease"], plot_width=800, plot_height=600, title="Number of occurrences of each disease in patho_niv1")
    p.hbar(y="Disease", right="Number of occurrences", source=source, height=0.5, color=color_mapper)
    p.add_tools(hover)

    st.bokeh_chart(p)

    st.write("Most patients have a disease in the circulatory system with 83.278 patients, cancer with 70.055 patients or an inflammatory or rare disease or HIV or AIDS with 60.333 patients. We can see that everyone has a disease.")

if selected_chart == "Patho_niv2":
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

if selected_chart == "Patho_niv3":
    st.title("Number of occurrences of each disease in patho_niv3")

    patho_niv1_counts = data["patho_niv3"].value_counts().reset_index()
    patho_niv1_counts.columns = ["Disease", "Number of occurrences"]

    patho_niv1_counts = patho_niv1_counts.sort_values(by="Number of occurrences", ascending=False)

    bars = alt.Chart(patho_niv1_counts).mark_bar().encode(
        y=alt.Y('Disease:N', sort='-x', axis=alt.Axis(labelLimit=0)),
        x=alt.X('Number of occurrences:Q'),
        color=alt.Color('Disease:N', scale=alt.Scale(scheme='plasma'), legend=None),
        tooltip=['Disease', 'Number of occurrences']
    ).interactive()

    text = bars.mark_text(
        align='left',
        baseline='middle',
        dx=3
    ).encode(
        text='Number of occurrences:Q'
    )

    chart = (bars + text).properties(
        width=800,
        height=600,
        title="Number of occurrences of each disease in patho_niv3"
    )

    st.altair_chart(chart)

    st.write("For this graph, we also see that most of the patients don't have a second sub-category disease, even more than the previous graph. Indeed, 123.844 patients don't have a second sub-category disease. However, there are some patients that do have a disease but the number is not very significant compared to our previous graphs. For instance, most patients have other long-term infection with 7558 patients and 7548 patients for occasional hospitalizations.")
