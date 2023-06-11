# -*- coding: utf-8 -*-
"""TSF internship task 1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EZangdqgm7OXLPEMEdQXqaxVRSFSX3W3

**Required libraries**
"""

import pandas as pd
import numpy as np  
import matplotlib.pyplot as plt

"""**Importing data**"""

url="http://bit.ly/w-data"
sample_data = pd.read_csv(url)
sample_data.head(10)

"""**Plotting hours vs scores**"""

sample_data.plot(x='Hours', y='Scores', style='o')  
plt.title('Hours vs Scores')  
plt.xlabel('Hours Studied')  
plt.ylabel('Score')  
plt.show()

x = sample_data.iloc[:, :-1].values  
y = sample_data.iloc[:, 1].values

"""**Splitting data for training and testing**"""

from sklearn.model_selection import train_test_split  
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=0)

"""**Fitting data to the Regression model**"""

from sklearn.linear_model import LinearRegression  
regressor = LinearRegression()  
regressor.fit(X_train, y_train) 
print("Completed Training")

"""**Plotting the Regression line**"""

m=regressor.coef_
c=regressor.intercept_
line = m*x+c

plt.scatter(x, y)
plt.plot(x, line);
plt.show()

y_pred = regressor.predict(X_test)

"""**Actual vs Predicted output**"""

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})  
df

"""**Predicted score if student studies for 9.25 hrs/day**"""

hours=9.25
own_pred = regressor.predict([[hours]])
print("No of Hours = {}".format(hours))
print("Predicted Score = {}".format(own_pred[0]))

"""**Mean Absolute Error**"""

from sklearn import metrics
print('Mean Absolute Error: ', metrics.mean_absolute_error(y_test, y_pred))