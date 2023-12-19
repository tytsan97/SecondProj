import pandas as pd
import streamlit as st

data= pd.read_csv("water_potability.csv")
st.title("Data Visualization for Water Quality Classification")
st.subheader("Dataset Shape")
st.write(data.shape)
num=data.describe()
st.write(num)
