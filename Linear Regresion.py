# """Linear Regression using Visulization"""
# import matplotlib.pylab as plt
# from scipy import stats
# import numpy as np

# X = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# Y = [99,86,87,88,111,86,103,87,94,78,77,85,86]
# color =  np.random.randint(1,100,13)
# size  = 4 * np.random.randint(1,20,13)
# slope,intercept,r,p,std_err = stats.linregress(X,Y)

# def myfun(X):
#     return slope * X + intercept
# mymodel = list(map(myfun,X))

# print(slope)
# print(r)
# plt.scatter(X,Y,cmap='flag',s=size,c=color,alpha=0.8)
# plt.plot(X,mymodel,'P-.',linewidth=2.5,mfc='blue',color='red')
# plt.show()

'''-----------------'''

# import  matplotlib.pyplot as plt
# from scipy import stats
# import numpy as np
# x = [12,21,31,44,35,56,73,82,29,20]
# y = [98,86,73,67,54,48,38,26,19,8]
# color = np.random.randint(1,100,10)
# size = 6 * np.random.randint(1,20,10)

# slope,intercept,r,p,std_err= stats.linregress(x,y)

# def MyFun(x):
#     return slope * x + intercept

# mymodel = list(map(MyFun,x))

# print('The coefficient of corelation is :',r)
# print('The p is :',p)
# print('The Slope is :',slope)
# print('The intercept is :',intercept)
# print('the std_err is :',std_err)

# plt.scatter(x,y,cmap='flag',alpha=0.8,c=color,s=size)
# plt.plot(x,mymodel,'P-.',linewidth=2.4,color='hotpink',markerfacecolor='blue',markeredgecolor='yellow')
# plt.show()

'''------------------'''

# import numpy as np
# import matplotlib.pyplot as plt
# import pandas
# from scipy import stats

# data = pandas.read_csv('D:/Python/File Handling/canada_per_capita_income.csv')
# print(data)

# x = data['year']
# y = data['per capita income (US$)']
# color = np.random.randint(1,100,47)
# size = np.random.randint(1,100,47)

# slope,intercept,r,p,std_err= stats.linregress(x,y)

# def MyFun(x):
#     return slope * x + intercept

# mymodel = list(map(MyFun,x))

# fonty = {'family':'century','size':16,'color':'pink'}
# fontx = {'family':'impact','size':16,'color':'green'}

# print('The Coeficient of Corelation is :',r)
# print('The slope is the :',slope)
# print('The Interception is :',intercept)
# print('the p is ',p)
# print('The Std is :',std_err)


# plt.scatter(x,y,c=color,s=size,cmap='Dark2')
# plt.plot(x,mymodel,'+-.',linewidth=4.2,markeredgecolor='black',markerfacecolor='yellow',color='green')
# plt.xlabel('Year',fontdict=fontx)
# plt.ylabel('Income',fontdict=fonty)
# plt.title('Canada per Capita income',family='impact',size=23,color='red')
# plt.show()

'''----------------------'''

# import numpy as np
# import matplotlib.pyplot as plt
# import pandas
# from scipy import stats

# Data = pandas.read_csv('D:/Python/File Handling/LineRegress.csv')
# print(Data.to_string())

# X = Data['year']
# Y = Data['per capita income (US$)']
# color = np.random.randint(1,100,47)
# size  = np.random.randint(1,100,47)

# slope,intercept,r,p,std_err = stats.linregress(X,Y)

# def Myfun(X):
#     return slope * X + intercept

# mymodel = list(map(Myfun,X))

# predict = Myfun()
# print(predict)

# fontx = {'family':'algerian','size':16,'color':'green'}
# fonty = {'family':'century','size':16,'color':'pink'}

# plt.scatter(X,Y,c=color,s=size,cmap='flag')
# plt.plot(X,mymodel,marker='*',ls='-',markeredgecolor='black',markerfacecolor='green',color='red',linewidth=2.4)
# plt.xlabel('Independent Var',fontdict=fontx)
# plt.ylabel('Dependent Var',fontdict=fonty)
# plt.title('Linear regression of canada per capita income',family='impact',size=20,color='yellow')
# plt.show()

''''''

# import numpy as np
# import pandas as pd
# from scipy import stats
# import matplotlib.pyplot as plt
# from sklearn import linear_model

# Data = pd.read_csv('D:/Python/File Handling/LinRegress.csv')
# print(Data.to_string())

# x = Data['year']
# y = Data['per capita income (US$)']
# size  = np.random.randint(1,100,47)
# color = np.random.randint(1,100,47)

# slope,intercept,r,p,std_err = stats.linregress(x,y)
# def Fun(x):
#     return slope * x + intercept
# Model = list(map(Fun,x))


# Year = int(input('\nEnter the Year to predict the income :'))
# predict = Fun(Year)
# print('\nThe Prediction of income as per the Year {0} is {1}.'.format(Year,predict))

# print(intercept)
# print(r)
# print(slope)


# plt.scatter(x,y,s=size,c=color,cmap='hot')
# plt.plot(x,Model,marker='H',ls='dotted',markerfacecolor='Yellow',markeredgecolor='blue',color='green',linewidth=5.5,)
# plt.xlabel('Year')
# plt.ylabel('Income')
# plt.title('Canada Income Vilulization')
# plt.show()

'''-------------------------'''


