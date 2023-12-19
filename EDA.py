import pandas as pd
import streamlit as st

data= pd.read_csv("/kaggle/input/water-potability/water_potability.csv")
st.title("Data Visualization for Water Quality Classification")
st.subheader("Dataset Shape")
st.write(data.shape)
