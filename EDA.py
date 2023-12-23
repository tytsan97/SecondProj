import pandas as pd
import streamlit as st
import plotly.express as px

data= pd.read_csv("water_potability.csv")
st.title("Data Visualization for Water Quality Classification")
st.subheader("Dataset Shape")
st.write(data.shape)

st.header('Distribution of Target')
hist_data = data['Potability']


# Create distplot with custom bin_size
fig = ff.create_distplot(hist_data)

# Plot!
st.plotly_chart(fig, use_container_width=True)
