import streamlit as st
st.title("MI PRIMER APP")
#st.button("dale click")
#st.button("otro botón")
import pandas as pd
df = pd.read_csv("https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv")
st.write(df)
st.map(df)