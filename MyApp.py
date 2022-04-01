import streamlit as st
st.title("MI PRIMER APP")
click=st.button("dale click")
st.write("el valor de click es ",click)
#st.button("otro botón")
import pandas as pd
#las siguientes tres lineas eran para elprimer ejercicio
df = pd.read_csv("https://raw.githubusercontent.com/quantum-apps/mapa/main/data.csv")
#st.write(df)
#st.map(df)
#st.text("HOLA MUNDO")
#st.text("la sigiente es una integral")
#st.latex(" \int ")
#st.markdown(" #titulo ")
#st.markdown(" *este es una viñeta* ")
#st.markdown(" **negritas** ")
