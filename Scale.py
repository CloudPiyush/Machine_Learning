'''Scaleing the Data and Predicting the Co2 Emission of Car.'''
# import pandas as pd
# from sklearn import linear_model
# from sklearn.preprocessing import StandardScaler

# Data = pd.read_csv('D:/Python/File Handling/Scale.csv')
# print(Data.to_string())

# x = Data[['Volume','Weight']]
# y = Data['CO2']

# Scale = StandardScaler()
# Scalex = Scale.fit_transform(x)      #Scaling the Volume and Weight to compare and Predict.
# print(Scalex)

# Regression = linear_model.LinearRegression()
# Regression.fit(Scalex,y)

# Scaled = Scale.transform([[1.0,790]])
# Predict = Regression.predict(Scaled)
# print(Predict)

'''Scaling the data'''

# import numpy as np
# import pandas as pd
# from sklearn.preprocessing import StandardScaler

# Data = pd.read_csv('D:/Python/File Handling/Scale.csv')
# print(Data.to_string())

# X = Data[['Volume','Weight']]

# Scale = StandardScaler()
# ScaleX = Scale.fit_transform(X)
# print('\nThe Standardization of Scaller is :{0}.'.format(ScaleX))

'''Predicting The CO2 Emission and Scale data'''

# import pandas as pd
# from sklearn.preprocessing import StandardScaler 
# from sklearn import linear_model

# Data = pd.read_csv('D:/Python/File Handling/Scale.csv')
# print(Data.to_string())

# X = Data[['Volume','Weight']]
# Y = Data['CO2']

# Scale = StandardScaler()
# ScaledX = Scale.fit_transform(X)

# Regression = linear_model.LinearRegression()
# Regression.fit(ScaledX,Y)

# Volume = float(input('\nEnter the Volume :'))
# Weight = int(input('\nEnter the Weight :'))

# Scaled  = Scale.transform([[Volume,Weight]])
# Predict = Regression.predict(Scaled)

# print('\nThe CO2 Emission of Car Volume {0} and Weight {1} is {2}.'.format(Volume,Weight,Predict))
# print('\nThe Standardization of Scale is :\n{0}.'.format(ScaledX))
