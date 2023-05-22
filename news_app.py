import streamlit as st
import requests
import pycountry
import apikey

st.title("News App")

col1, col2 = st.columns([3,1])
with col1:
    user = st.text_input("Enter Country Name")

with col2:
    category = st.radio('Choose Category',('Technology','Politics','Sports','Business','Finance'))
    btn = st.button('Enter')

if btn:
    country = pycountry.countries.get(name=user).alpha_2
    url=f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}"
