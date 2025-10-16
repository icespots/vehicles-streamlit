import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Vehicles EDA", layout="wide")

st.header("Análisis de anuncios de coches")

# CargSa de datos


@st.cache_data
def load_data():
    return pd.read_csv("vehicles_us.csv")


car_data = load_data()

st.write("Primeras filas del dataset:")
st.dataframe(car_data.head())

# --- Controles con casillas de verificación (checkboxes) ---

# Histograma
build_hist = st.checkbox("Mostrar histograma (odometer)")
if build_hist:
    st.write("Creación de un histograma para **odometer**")
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Dispersión
build_scatter = st.checkbox("Mostrar dispersión (odometer vs price)")
if build_scatter:
    st.write("Gráfico de dispersión: **odometer** vs **price**")
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)
