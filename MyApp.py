import streamlit as st
st.title("MI PRIMER APP")
click=st.button("dale click")
st.write("el valor de click es ",click)
if click==True:
    st.image("https://www.efeverde.com/storage/2018/09/ARCHIVO-foca-monje-EFEverde.jpg")


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
num1 = st.slider('elige el número 1', 0, 130, 25)
num2 = st.slider('elige el número 2', 0, 130, 25)
suma = num1+num2
st.write("la suma de",num1,"y",num2,"es:",suma)