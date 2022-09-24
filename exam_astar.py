# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 15:57:05 2022

@author: DELL
"""

def aStarAlgo(start_node,stop_node):
    open_set=set(start_node)
    close_set=set()
    g={}
    parent={}
    g[start_node]=0
    parent[start_node]=start_node
    while len(open_set)>0:
        n=None
        for v in open_set:
            if n== None or g[v]+heuristic[v]<g[n]+heuristic(n):
                n=v
        if n== stop_node or Graph_nodes[n]==None:
            pass
        else:
            for (m,weight) in getNeighbors(n):
                if m not in close_set and m not in open_set:
                    open_set.add(m)
                    parent[m]=n
                    g[m]=g[n]+weight
                else:
                    if g[m]>g[n]+weight:
                        g[m]=g[n]+weight
                        parent[m]=n
                    if m in close_set:
                        close_set.remove(m)
                        open_set.add(m)
        if n==None:
            print('Path does not exist')
            return None
        if n==stop_node:
            path=[]
            while parent[n]!=n:
                path.append(n)
                n=parent[n]
            path.append(start_node)
            path.reverse()
            print('path'.format(path))
            return path
        open_set.remove(n)
        close_set.add(n)
        print('path does not exist')
        return None
def heuristic(n):
    H_dist={
       'A' :11,
        'B':6,
        'C':99,
        'D':1,
        'E':7,
        'G':0
        }
def getNeighbors(v):
    if v in Graph_nodes:
        return Graph_nodes[v]
    else:
        return None
Graph_nodes={
    'A':[('B',2),('E',3)],
    'B':[('C',1),('G',9)],
    
    'E':[('D',6)],
    'D':[('G',1)]
    }
aStarAlgo('A','G')