# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 21:17:59 2022

@author: DELL
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
X=np.array(([2,9],[1,5],[3,6]),dtype=float)
Y=np.array(([92],[86],[89]),dtype=float)
X=X/np.amax(X,axis=0)
Y=Y/100
def sigmoid(x):
    return 1/(1+np.exp(-x))
def derivatives_sigmoid(x):
    return x*(1-x)
A=[]
B=[]
for i in range (5):
    epoch=700*i
    A.append(epoch)
    lr=0.1
    i=2
    h=3
    o=1
    wh=np.random.uniform(size=(i,h))
    bh=np.random.uniform(size=(1,h))
    wout=np.random.uniform(size=(h,o))
    bout=np.random.uniform(size=(1,0))
start_time=time.time()
for i in range(epoch):
    hinp1=np.dot(X,wh)
    hinp=hinp1+bh
    hlayer_act=sigmoid(hinp)
    outinp1=np.dot(hlayer_act,wout)
    outinp=outinp1+bout
    output=sigmoid(outinp)
    EO=Y-output
    outgrad=derivatives_sigmoid(output)
    d_output=EO*outgrad
    EH=d_output.dot(wout.T)
    hiddengrad=derivatives_sigmoid(hlayer_act)
    d_hiddenlayer=EH*hiddengrad
    wout+=hlayer_act.T.dot(d_output)*lr
    wh+=X.T.dot(d_hiddenlayer)*lr
    bout+=np.sum(d_output,axis=0,keepdims=True)*lr
    bh+=np.sum(d_hiddenlayer,axis=0,keepdims=True)*lr
B.append(time.time()-start_time)
plt.plot(A,B)
plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.title('My first graph')
plt.show()
print('Input'+str(X))
print('Actual'+str(Y))
print('Predict',output)