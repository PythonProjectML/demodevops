# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 00:24:23 2022

@author: DELL
"""

import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import preprocessing
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import pandas as pd
import numpy as np
iris=datasets.load_iris()
X=pd.DataFrame(iris.data)
Y=pd.DataFrame(iris.target)
X.columns=['sepal_length','sepal_width','petal_length','petal_width']
Y.columns=['Targets']
model=KMeans(n_clusters=3)
model.fit(X)
plt.figure(figsize=(14,14))
colormap=np.array(['lime','red','black'])

plt.subplot(2,2,1)
plt.title('Real Clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal width')
plt.show()
plt.subplot(2,2,2)
plt.title('KMeans Clustering')                  
plt.xlabel('Petal Length')
plt.ylabel('Petal width')
plt.show()
scaler=preprocessing.StandardScaler()
scaler.fit(X)
xs=pd.DataFrame(scaler.transform(X),columns=X.columns)

gmm=GaussianMixture(n_components=3)
gmm.fit(X)
gmm_y=gmm.predict(xs) 
plt.subplot(2,2,3)
plt.title('GMM clustering')
plt.xlabel('Petal Length')
plt.ylabel('Petal width')
plt.show()          