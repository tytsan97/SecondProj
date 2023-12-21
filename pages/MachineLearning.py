import pandas as pd
import streamlit as st

df = pd.read_csv("water_potability.csv")
ph = st.number_input("Enter pH Level:")
st.write(ph)
hard = st.number_input("Enter amount of Hardness:")
st.write(hard)
solid = st.number_input("Enter amount of Solids:")
st.write(solid)
