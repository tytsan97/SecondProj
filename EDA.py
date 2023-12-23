import pandas as pd
import streamlit as st
import plotly.express as px

data= pd.read_csv("water_potability.csv")
st.title("Data Visualization for Water Quality Classification")
st.subheader("Dataset Shape")
st.write(data.shape)

st.header('Distribution of Target')
plot = sns.heatmap(data.corr(), annot=True)
 
# Display the plot in Streamlit
st.pyplot(plot.get_figure())
