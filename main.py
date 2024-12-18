import streamlit as st
import pandas

st.set_page_config(layout="wide")

col1,col2 = st.columns(2)

with col1:
    st.image("images/photo.png")
with col2:
    st.title("Jothi")
    content = """Hi,I am jothi.I am a python developer working in Tata consultancy services."""
    st.info(content)

st.write("Below you can add some features and description to explain the user to understand more about the app ")

col3,col4 = st.columns(2)

dataframe = pandas.read_csv("data.csv",sep=";")
with col1:
    for index,row in dataframe[:10].iterrows():
        st.header(row["title"])

with col2:
    for index, row in dataframe[10:].iterrows():
        st.header(row["title"])


