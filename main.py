# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import streamlit as st
import pandas as pd
import plotly.express as px


df = px.data.gapminder()
st.dataframe(df)
listaPaises = df["country"].unique().tolist()
st.write(listaPaises)

st.header("Hola desde Streamlit!")
st.subheader("Probando ..1..2..3")
st.write("Hola soy Jess")
st.write("modificando codigo")
pais="Canada"

with st.sidebar:
    st.write("Esta es una barra lateral")
    pais = st.selectbox(
        'Meses del año', listaPaises)

    st.write('You selected:', pais)

datosPais = df.query("country == '" + pais+"'")
fig = px.bar(datosPais, x='year', y='pop')
st.plotly_chart(fig, use_container_width=True)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
