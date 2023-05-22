import streamlit as st
import pandas


df = pandas.read_csv('hrdata.csv')
print(df)
st.dataframe(df)
