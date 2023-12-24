import pandas as pd
import streamlit as st
import plotly.express as px

import matplotlib.pyplot as plt
data= pd.read_csv("water_potability.csv")
st.title("Data Visualization for Water Quality Classification")
st.subheader("Dataset Shape")
st.write(data.shape)
data['ph']=data['ph'].fillna(value=data['ph'].median())
data['Sulfate']=data['Sulfate'].fillna(value=data['Sulfate'].median())
data['Trihalomethanes']=data['Trihalomethanes'].fillna(value=data['Trihalomethanes'].median())
st.header('Distribution of Target')
fig, ax = plt.subplots()
ax.hist(data['Potability'])
st.pyplot(fig)
st.subheader("This is unbalance distribution , 0 values is more than 1 values.")
st.header("Statistical Value")
num=data.describe()
st.write(num)
st.header("Correlation Features and Target")
corr=pd.DataFrame(data.corr())
corr
st.header("Factors Affecting Water Quality: pH")
fig = px.histogram(data,x="ph",color="Potability")
fig

st.header("Factors Affecting Water Quality: Solid")
fig = px.histogram(data,x="Solids",color="Potability")
fig

st.header("Factors Affecting Water Quality: Sulfate")
fig = px.histogram(data,x="Sulfate",color="Potability")
fig
st.write()
st.header("Factors Affecting Water Quality: Chloramines")
fig = px.histogram(data,x="Chloramines",color="Potability")
fig
st.write()
st.header("Factors Affecting Water Quality: Organic_Carbon")
fig = px.histogram(data,x="Organic_carbon",color="Potability")
fig
st.write()
st.header("Factors Affecting Water Quality: Trihalomethanes")
fig = px.histogram(data,x="Trihalomethanes",color="Potability")
fig
st.write()
st.header("Factors Affecting Water Quality: Turbidity")
fig = px.histogram(data,x="Turbidity",color="Potability")
fig
st.write()
st.header("Factors Affecting Water Quality: Conductivity")
fig = px.histogram(data,x="Conductivity",color="Potability")
fig
st.write()

