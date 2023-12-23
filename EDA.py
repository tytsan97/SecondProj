
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.figure_factory as ff
import matplotlib.pyplot as plt
data= pd.read_csv("water_potability.csv")
st.title("Data Visualization for Water Quality Classification")
st.subheader("Dataset Shape")
st.write(data.shape)

st.header('Distribution of Target')
fig, ax = plt.subplots()
ax.hist(data['Potability'])
st.pyplot(fig)
st.write("Thisisunbalancedistribution,0ismorethan1.")
corr=data.corr()
st.subheader(corr)
