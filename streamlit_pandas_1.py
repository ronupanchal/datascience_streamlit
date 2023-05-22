import streamlit as st
import pandas


df = pandas.read_csv('hrdata.csv')
print(df)
st.dataframe(df)

# print(type(df['Hire Date'][0]))

# df = pandas.read_csv('hrdata.csv', index_col='Name')
# print(df)

# df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
# print(df)