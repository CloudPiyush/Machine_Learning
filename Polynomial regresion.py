# import numpy as np
# import matplotlib.pyplot as plt
# import pandas as pd
# from sklearn.metrics import r2_score

# Data = pd.read_csv('D:/Python/File Handling/PolyRegress.csv')
# X = Data['Hours']
# Y = Data['Speed']

# size  = np.random.randint(1,100,18)
# color = np.random.randint(1,100,18)

# Polynomial_Regression = np.poly1d(np.polyfit(X,Y,3)) #Calculating Polynomial Regression
# MyModel = np.linspace(1,22,100)                      

# Time  = int(input('\nEnter the Time to predict the Speed of Car :'))
# Speed = Polynomial_Regression(Time)                  #Predicting Future of Car Speed

# print('\nThe Speed of Car at Time {0} Will Be {1}.'.format(Time,Speed))
# print('\nThe R-Squared is  :{0}'.format(r2_score(Y,Polynomial_Regression(X))))

# fontx = {'family':'algerian','color':'red','size':16}
# fonty = {'family':'century','color':'blue','size':18}

# plt.scatter(X,Y,s=size,c=color,cmap='cool',alpha=0.7)
# plt.plot(MyModel,Polynomial_Regression(MyModel),'H--',mfc='red',mec='yellow',color='green',linewidth='5.3')
# plt.xlabel('Hours of Car Going',fontdict=fontx)
# plt.ylabel('Speed of Cars',fontdict=fonty)
# plt.title('Polynomial Regression of car and Speed.',family='impact',color='red',size=23)
# plt.show()

'''------------------------'''

# import numpy as np
# import matplotlib.pyplot as plt
# import pandas
# from scipy import stats

# data = pandas.read_csv('D:/Python/File Handling/Cars.csv')
# print(data)

# x = data['Hours']
# y = data['Speed']
# color = np.random.randint(1,100,18)
# size = np.random.randint(1,100,18)

# mymodel = np.poly1d(np.polyfit(x,y,3))
# myline  = np.linspace(1,25,100)

# fonty = {'family':'century','size':16,'color':'pink'}
# fontx = {'family':'impact','size':16,'color':'green'}

# plt.scatter(x,y,c=color,s=size,cmap='Dark2')
# plt.plot(myline,mymodel(myline),'+-.',linewidth=4.2,markeredgecolor='black',markerfacecolor='yellow',color='pink')
# plt.xlabel('Hours',fontdict=fontx)
# plt.ylabel('Speed',fontdict=fonty)
# plt.title('Cars Speed Visulization',family='impact',size=23,color='red')
# plt.show()

'''--------------------'''

# import matplotlib.pyplot as plt
# import pandas as pd
# import numpy  as np
# from sklearn.metrics import r2_score
# from scipy import stats

# Data = pd.read_csv('D:/Python/File Handling/PolyRegress.csv')
# print(Data.to_string())

# x = Data['Hours']
# y = Data['Speed']
# size  = np.random.randint(1,100,18)
# color = np.random.randint(1,100,18)


# Model = np.poly1d(np.polyfit(x,y,3))
# line = np.linspace(1,24,100)

# Hour = int(input('\nEnter the  Hour to predict the speed :'))
# Predict = Model(Hour)
# print(Predict)

# fontx = {'family':'century','color':'green','size':'14'}
# fonty = {'family':'impact','color':'red','size':'14'}
# font  = {'family':'algerian','color':'salmon','size':'24'}
# plt.scatter(x,y,c=color,s=size,cmap='cool')
# plt.plot(line,Model(line),marker='H',markeredgecolor='yellow',markerfacecolor='red',color='pink')
# plt.xlabel('Hours',fontdict=fontx)
# plt.ylabel('Speed',fontdict=fonty)
# plt.title('Polynomal regression Analysis of Data',fontdict=font)
# plt.show()