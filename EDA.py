import pandas as pd
import streamlit as st
import plotly.express as px

data= pd.read_csv("water_potability.csv")
st.title("Data Visualization for Water Quality Classification")
st.subheader("Dataset Shape")
st.write(data.shape)

st.header('Distribution of Classes')
fig = px.pie(data,names ="Potability",hole = 0.4,template ="plotly_dark")
fig.show()
fig1 = px.scatter(data,x='ph',y='Sulfate',color="Potability")
plotly_events(fig1)
