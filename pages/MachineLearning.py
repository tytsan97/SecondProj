import pandas as pd
import streamlit as st

df = pd.read_csv("water_potability.csv")
st.write(df)
