'''Draw the Decision tree '''

# import pandas as pd
# from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt

# Data = pd.read_csv('D:/Python/File Handling/Decision_Tree.csv')

# D1 = {'UK':0,'USA':1,'N':2}
# Data['Nationality'] = Data['Nationality'].map(D1)

# D2 = {'YES':1,'NO':0}
# Data['Go'] = Data['Go'].map(D2)

# Features = ['Age','Experience','Rank','Nationality']

# print(Data)

# X = Data[Features]
# Y = Data['Go']

# Dtree = DecisionTreeClassifier()
# Dtree.fit(X,Y)

# tree.plot_tree(Dtree,feature_names=Features)
# plt.show()

'''Predict the Values Base on Decision Tree.'''

# from sklearn import tree
# import matplotlib.pyplot as plt
# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier

# Data = pd.read_csv('D:/Python/File Handling/Decision_Tree.csv')
# print(Data.to_string())

# D1 = {'UK':0,'USA':1,'N':2}
# Data['Nationality'] = Data['Nationality'].map(D1)

# D2 = {'YES':1,'NO':0}
# Data['Go'] = Data['Go'].map(D2)

# Features = ['Age','Experience','Rank','Nationality']

# X = Data[Features]
# Y = Data['Go']

# Dtree = DecisionTreeClassifier()
# Dtree.fit(X,Y)

# Prediction = (Dtree.predict([[45,9,9,0]]))
# print(Prediction)

# tree.plot_tree(Dtree,feature_names=Features)
# plt.show()


'''Draw Tree And Predict the Values.'''

# import pandas as pd
# from sklearn import tree
# from sklearn.tree import DecisionTreeClassifier
# import matplotlib.pyplot as plt

# Data = pd.read_csv('D:/Python/File Handling/Decision_Tree.csv')
# print(Data.to_string())

# D1 = {'UK':0,'USA':1,'N':2}
# Data['Nationality'] = Data['Nationality'].map(D1)

# D2 = {'YES':1,'NO':2}
# Data['Go'] = Data['Go'].map(D2)

# Features = ['Age','Experience','Rank','Nationality']

# X = Data[Features]
# Y = Data['Go']

# Tree_model = DecisionTreeClassifier()
# Tree_model.fit(X,Y)

# tree.plot_tree(Tree_model,feature_names=Features)
# plt.show()

'''-------------'''

# import pandas as pd
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn import tree
# import matplotlib.pyplot as plt

# pd.options.display.max_rows = 1000

# Data = pd.read_csv('D:/Python/File Handling/Titanic_Data.csv')
# Data
# Data.drop(['Pclass','Name','SibSp','Ticket','Embarked','Cabin'],axis='columns',inplace=True)
# Data
# from sklearn.preprocessing import LabelEncoder
# Encode = LabelEncoder()
# Data['Sex'] = Encode.fit_transform(Data['Sex'])
# Data['Age'] = Data.Age.fillna(Data['Age'].median())
# Data.head()

# Feature = ['PassengerId','Sex','Age','Fare']
# X = Data[Feature]
# Y = Data['Survived']
# from sklearn.model_selection import train_test_split
# from sklearn.tree import DecisionTreeClassifier
# Model = DecisionTreeClassifier()
# Xtr , Xts , Ytr , Yts = train_test_split(X,Y,test_size=0.4)

# Model.fit(Xtr,Ytr)
# Model.score(Xtr,Ytr)
# Model.predict([[2,0,38,71]])

# tree.plot_tree(Model,feature_names=Feature)
# plt.show()

'''Decision tree using the Data-set'''

# from sklearn.datasets import load_iris
# from sklearn.tree import DecisionTreeClassifier
# from sklearn.model_selection import train_test_split
# from sklearn import tree
# from matplotlib import pyplot
# import pandas as pd

# Data = load_iris()

# print('\nThe Data of Dataset is :{0}.\n'.format(dir(Data)))

# File = pd.DataFrame(Data.data,columns=Data.feature_names)
# File['Target'] = Data.target
# print(File.head)

# Feature = ['sepal length (cm)','sepal width (cm)','petal length (cm)','petal width (cm)']

# X = File[Feature]
# Y = File['Target']

# X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=1)

# Tree = DecisionTreeClassifier()
# Tree.fit(X_train,y_train)
# print('\nThe Accurecy is the  :',Tree.score(X_test,y_test))

# tree.plot_tree(Tree,feature_names=Feature)
# pyplot.show()

