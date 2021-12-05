import streamlit as st
import pandas as pd
import plotly.express as px
import os

DATAFILE = os.path.join("data", "live_data.csv")

df = pd.read_csv (DATAFILE)
clist = df['Name'].unique()
name = st.sidebar.selectbox("Select an item:",clist)
st.header("Item cost over time")
fig = px.line(df[df['Name'] == name],
    x = "Time", y = "Cost", title = name)
st.plotly_chart(fig)