# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:47:35 2022

@author: DELL
"""

import numpy as np
import pandas as pd
data=pd.DataFrame(pd.read_csv('finds.csv'))
concepts=np.array(data.iloc[:,0,-1])
target=np.array(data.iloc[:,-1])
def learn(concepts,target):
    specific_h=[0,0,0,0,0,0]
    print("s0",specific_h)
    specific_h=concepts[0].copy()
    print("s1",specific_h)
    general_h=[["?" for i in range (len(specific_h))]for i in range (len(specific_h))]
    print("g0",general_h)
    for i,h in enumerate(concepts):
        if target == "YES":
            for x in range (len(specific_h)):
                if h[x]!=specific_h:
                    specific_h='?'
                    general_h[x][x]='?'
                    print(f"s[x]",specific_h)
                    print(f"g[x]",general_h)
        if target == "NO":
            for x in range (len(specific_h)):
                if h[x]!=specific_h:
                    general_h[x][x]=specific_h
                else:
                    general_h[x][x]='?'
    indices=[i for i,val in enumerate(general_h)if val == ['?','?','?','?','?','?']]
    for i in indices:
        general_h.remove(['?','?','?','?','?','?'])
        print('i',indices)
    return specific_h,general_h
s_final,g_final=learn(concepts,target)
    
    
                    