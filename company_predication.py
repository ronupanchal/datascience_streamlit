import streamlit as st

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import confusion_matrix
import plotly.express as px

data = pd.read_csv("https://raw.githubusercontent.com/ronupanchal/ML_Algorithm_code/main/Company.csv")
data.head()

st.dataframe(data, use_container_width=True)

#Assign the experience in real_x
real_x = data.iloc[:,0].values
#real_x

real_x=real_x.reshape(-1,1)
#real_x

#Assign the salary  in real_y
real_y = data.iloc[:,1].values
#real_y

real_y=real_y.reshape(-1,1)
#real_y
     
training_x, testing_x, training_y, testing_y = train_test_split(real_x,real_y,test_size=0.3,random_state=0)


Lin=LinearRegression()
Lin.fit(training_x,training_y)

Pred_y = Lin.predict(testing_x)

testing_y[3]

Pred_y[3]

fig = plt.figure(figsize=(8,8))

plt.scatter(training_x, training_y, color='green')
plt.plot(training_x, Lin.predict(training_x),color='blue')
plt.title("Salary & Exp training plot")
plt.xlabel("Exp")
plt.ylabel("Salary")
plt.show()

st.pyplot(fig) 


plt.scatter(testing_x, testing_y, color='green')
plt.plot(training_x, Lin.predict(training_x),color='blue')
plt.title("Salary & Exp testing plot")
plt.xlabel("Exp")
plt.ylabel("Salary")
st.pyplot(fig)

#Y = b1x + b0
st.text(f"coefficient:{Lin.coef_}")

st.text(f"intercept:{Lin.intercept_}")


# Short answer is no you cannot use a confusion matrix for a regression
# results = confusion_matrix(testing_y, Pred_y)
# print(results)
