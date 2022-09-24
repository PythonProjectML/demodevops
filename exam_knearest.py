# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 16:52:09 2022

@author: DELL
"""

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn import datasets
iris=datasets.load_iris()
x_train,x_test,y_train,y_test=train_test_split(iris.data,iris.target,test_size=0.1)
print('Training data',x_train.shape,y_train.shape)
print('Testing data',x_test.shape,y_test.shape)

for i in range(len(iris.target_names)):
    print(iris.target_names[i])
    
classifier=KNeighborsClassifier(n_neighbors=1)
classifier.fit(x_train,y_train)
y_pred=classifier.predict(x_test)

for r in range(0,len(x_test)):
    print('Sample',str(x_test[r]))
    print('Actual',str(y_test[r]))
    print('Predict',str(y_pred[r]))

print(classifier.score(x_test,y_test))
print('Accuracy',classification_report(y_test, y_pred))
print('Confusion Matrix',confusion_matrix(y_test, y_pred))

 