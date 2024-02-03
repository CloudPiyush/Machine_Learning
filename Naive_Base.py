import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn.model_selection import cross_val_score

pd.options.display.max_rows = 999
Data = pd.read_csv('D:/Python/File Handling/Titanic_Data.csv')
Data.drop(['PassengerId','Name','Cabin','Embarked','Parch','SibSp','Ticket'],axis='columns',inplace=True)
print(Data)

Independent = Data.drop('Survived',axis='columns')
Target = Data.Survived

#print(Independent)

Dumies = pd.get_dummies(Independent['Sex'])
#print(Independent)

Input = pd.concat([Independent,Dumies],axis='columns')
#print(Input)

Input.drop(['female','Sex'],axis='columns',inplace=True)
#print(Input)

Encode = LabelEncoder()
Input['male'] = Encode.fit_transform(Input['male'])
#print(Input)

print(Input.columns[Input.isna().any()])
#print(Input.Age)

Input['Age'] = Input['Age'].fillna(Input.Age.mean())
#print(Input.Age)

X_train, X_test, y_train, y_test = train_test_split(Input,Target,test_size=0.2,random_state=7)

Model = naive_bayes.GaussianNB()
Model.fit(X_train,y_train)
print(X_train[0:10])
print(Model.predict_proba([[1,39,83,0]]))
print(cross_val_score(naive_bayes.GaussianNB(),X_train,y_train,cv=3))

Survivel_Prediction_Xtrain = Model.predict(Input)
print(Survivel_Prediction_Xtrain)
Survivel_x = Survivel_Prediction_Xtrain

Input['Survivel_Predict'] = Survivel_x

#print(Input.to_csv('D:/Python/File Handling/Tatanic_Naive_Predict.csv'))
print(Input)