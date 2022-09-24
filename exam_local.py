# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 09:43:55 2022

@author: DELL
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
def kernel(point,xmat,k):
    m,n=np.shape(xmat)
    weight=np.mat(np.eye(m))
    for j in range(m):
        diff=point-X[j]
        weight[j,j]=np.exp((diff*diff.T)/(-2.0*k**2))
    return weight

def localWeight(point,xmat,ymat,k):
    w=kernel(point,xmat,k)
    B=(X.T*(w*X)).I*(X.T*(w*ymat.T))
    return B

def localWeightRegression(xmat,ymat,k):
    m,n=np.shape(xmat)
    ypred=np.zeros(m)
    for i in range(m):
        ypred[i]=xmat[i]*localWeight(xmat[i],xmat,ymat,k)
    return ypred

def graphPlot(X,ypred):
    sortindex=X[:,1].argsort(0)
    xsort=X[sortindex][:,0]
    fig=plt.figure()
    ax=fig.add_subplot(1,1,1)
    ax.scatter(bill,tip,3)
    ax.plot(xsort[:,1],ypred[sortindex],color='red',linewidth=5)
    plt.xlabel('x-axis')
    plt.ylabel('y-axis')
    plt.show()

    
data=pd.read_csv('data_tips.csv')
bill=np.array(data.total_bill)
tip=np.array(data.tip)
mbill=np.mat(bill)
mtip=np.mat(tip)
m=np.shape(mbill)[1]
one=np.mat(np.ones(m))
X=np.hstack((one.T,mbill.T))
ypred=localWeightRegression(X,mtip,3)
graphPlot(X,ypred)