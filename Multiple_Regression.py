
# import pandas as pd
# from sklearn import linear_model

# Data = pd.read_csv('D:/Python/File Handling/Multiregress.csv')
# print(Data.to_string())

# x = Data[['Weight','Volume']]
# y = Data['CO2']

# MultipleRegression = linear_model.LinearRegression()
# MultipleRegression.fit(x,y)

# Volume = int(input('\nEnter the Volume of Car :'))
# Weight = int(input('\nEnter tne Weight of Car :'))
# Prediction  = MultipleRegression.predict([[Volume,Weight]])
# Coefficient = MultipleRegression.coef_

# print('\nThe Emmision of \'Co2\' from car is :{0}'.format(Prediction))
# print('\nThe Coefficient of Multiple Regression is :{0}'.format(Coefficient))

'''Prediction of Data and Fittting the Data to another file File With Full Reading of Co2 Emmision.'''

import numpy as np
from  sklearn import linear_model
import pandas

Data = pandas.read_csv('D:/Python/File Handling/MultiRegress.csv')
print(Data.to_string())

x = Data[['Volume','Weight']]
y = Data['CO2']
color = np.random.randint(1,100,36)
size  = np.random.randint(1,100,36)

Regression = linear_model.LinearRegression()
Regression.fit(x,y)

New_Data = pandas.read_csv('D:/Python/File Handling/MultiRegress_Predicted.csv')
print(New_Data)


Predict = Regression.predict(New_Data)

New_Data['Co2_Emission'] = Predict
print(New_Data)

Volume = int(input('\nEnter the Volume of car :'))
Weight = int(input('\nEnter the Weight of car :'))

Predict = Regression.predict([[Volume,Weight]])
print('\nThe Prediction of CO2 of Car as per {0} Volume and {1} Weight will be :{2}'.format(Volume,Weight,Predict))
print('\nThe Coefficient  is :{0}'.format(Regression.coef_))
print('\nThe Intercept is :{0}'.format(Regression.intercept_))

print(Volume * Regression.coef_[0] + Weight * Regression.coef_[1] + Regression.intercept_)