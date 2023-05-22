
import pandas as pd
import streamlit as st
import numpy as np

df = pd.read_csv('hrdata.csv')
print(df)

st.dataframe(df)
st.dataframe(df.columns)
chart_data = pd.DataFrame(np.random.randn(20, 2), columns=['Name', 'Salary'])

st.bar_chart(chart_data, x='Name', y='Salary')

st.line_chart(chart_data)

# print(type(df['Hire Date'][0]))

# df = pandas.read_csv('hrdata.csv', index_col='Name')
# print(df)

# df = pandas.read_csv('hrdata.csv', index_col='Name', parse_dates=['Hire Date'])
# print(df)