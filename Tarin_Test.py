'''Our data set illustrates 100 customers in a shop, and their shopping habits.'''
# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(2)

# X = np.random.normal(3,1,100)       # X Represent customer timeperiod in grosery.    
# Y = np.random.normal(150,40,100)/X  # Y Represent Amount of Customer Purchase product as per time. 

# plt.scatter(X,Y)
# plt.show()

'''Using Train/Test'''

# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(7)

# X = np.random.normal(3,1,100)       # X Represent customer timeperiod in grosery.    
# Y = np.random.normal(150,40,100)/X  # Y Represent Amount of Customer Purchase product as per time. 

# Train_X = X[:80]
# Train_Y = Y[:80]

# Test_X = X[80:]
# Test_Y = Y[80:]

# plt.scatter(Train_X,Train_Y)
# plt.scatter(Test_X,Test_Y)
# plt.show()

'''Above Data Set is Fit With the Polynimial Regression.'''

# import numpy as np
# import matplotlib.pyplot as plt

# np.random.seed(2)

# X = np.random.normal(3,1,100)
# Y = np.random.normal(150,40,100)/X
# color = np.random.randint(1,100,80)
# size  = np.random.randint(1,100,80)

# Train_X = X[:80]
# Train_Y = Y[:80]

# Test_X  = X[80:]
# Test_Y  = Y[80:]

# Regression = np.poly1d(np.polyfit(Train_X,Train_Y,4))
# line = np.linspace(0,6,100)

# plt.scatter(Train_X,Train_Y,s=size,c=color,cmap='cool',alpha=0.5)
# #plt.scatter(Test_X,Test_Y,s=size,c=color,cmap='cool',alpha=0.8)
# plt.plot(line,Regression(line),marker='H',linewidth=2.4,mec='blue',mfc='yellow',color='pink',ls='-.')
# plt.show()

'''measures the relationship between the x axis and the y axis use the R-Squared'''

# import numpy as np
# from sklearn.metrics import r2_score

# np.random.seed(2)

# X = np.random.normal(3,1,100)
# Y = np.random.normal(150,40,100)/X

# Train_X = X[:80]
# Train_Y = Y[:80]

# Test_X  = X[80:]
# Test_Y  = Y[80:]

# Regression = np.poly1d(np.polyfit(Train_X,Train_Y,4))

# R_Squared = r2_score(Test_Y,Regression(Test_X))     #measurung relation 
##R_Squared = r2_score(Train_Y,Regression(Train_X))
# print('\nThe Relation Between The X and Y Axis is :',R_Squared)


"""Predict The Rsult That How Many Doller to spend by customer From perticular time Period"""

# # import numpy as np
# # import matplotlib.pyplot as plt
# # from sklearn.metrics import r2_score

# # np.random.seed(2)

# # X = np.random.normal(3,1,100)
# # Y = np.random.normal(150,40,100)/X
# # color = np.random.randint(1,100,80)
# # size  = np.random.randint(1,100,80)

# # Train_X = X[:80]
# # Train_Y = Y[:80]

# # Test_X =  X[80:]
# # Test_Y =  Y[80:]

# # Regression = np.poly1d(np.polyfit(Train_X,Train_Y,4))
# # line = np.linspace(0,6,100)

# # Minute = int(input('\nEnter the minute to Calculate Spending Dollor :'))
# # Predict = Regression(Minute)

# # print('\nThe Prediction of doller is :{0}.'.format(Predict))
# # print('\nThe Train Relation Between the X-Axis and Y-Axis is :{0}.'.format(r2_score(Train_Y,Regression(Train_X))))
# # print('\nThe Test  Realtion Between the X-Axis And Y-Axis is :{0}.'.format(r2_score(Test_Y,Regression(Test_X))))

# # plt.scatter(Train_X,Train_Y,s=size,c=color,cmap='cool',alpha=0.5)
# # plt.scatter(Test_X,Test_Y,s=size,c=color,cmap='cool',alpha=0.8)
# plt.plot(line,Regression(line),marker='H',linewidth=2.4,mec='blue',mfc='yellow',color='pink',ls='-.')
# plt.show()

