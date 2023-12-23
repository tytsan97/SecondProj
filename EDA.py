import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
data= pd.read_csv("water_potability.csv")
st.title("Data Visualization for Water Quality Classification")
st.subheader("Dataset Shape")
st.write(data.shape)

st.header('Distribution of Target')
st.bar_chart(data)
