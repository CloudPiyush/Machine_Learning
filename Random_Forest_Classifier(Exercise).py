from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from matplotlib import pyplot
import seaborn
from sklearn.datasets import load_iris
import pandas as pd
import sklearn.metrics
Data = load_iris()
print(dir(Data))

File = pd.DataFrame(Data.data,columns=Data.feature_names)
File['target'] = Data.target
File['Target Name'] = File.target.apply(lambda x: Data.target_names[x])
print(File)
X = File.drop(['target','Target Name'],axis='columns')
Y = File['target']
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.2,random_state=2)

Model = RandomForestClassifier(n_estimators=10)
Model.fit(X_train,y_train)

print('\nThe Training Model Accurecy is :'.format(Model.score(X_test,y_test)))
print('\nThe Testing  Model Accurecy is :'.format(Model.score(X_train,y_train)))
print('\nThe Length of training Model is :{0}'.format(len(X_train)))
print('\nThe Length of testing Model is :{0}'.format(len(X_test)))
print(Model.predict([['4.6','3.6','1.0','0.2']]))

predict = Model.predict(X_train)

CM = sklearn.metrics.confusion_matrix(y_train,predict)
print('\nThe Confusion Matrix of testing is :\n',CM)

fontx = {'family':'impact','color':'blue','size':16}
fonty = {'family':'century','color':'green','size':16}

pyplot.figure(figsize=(5,6))
seaborn.heatmap(CM,annot=True)
pyplot.xlabel('Predicted',fontdict=fontx)
pyplot.ylabel('Truth',fontdict=fonty)
pyplot.title('Confusion Matrix of Iris Data Using the Random Forest classifier',family='impact',color='red',size=20)
pyplot.show()