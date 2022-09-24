# -*- coding: utf-8 -*-
"""
Created on Tue Mar 15 23:35:15 2022

@author: DELL
"""

class Graph:
    def _init_ (self,graph,heuristic,startNode):
        self.graph=graph
        self.H=heuristic
        self.start=startNode
        self.parent={}
        self.status={}
        self.solutionGraph={}
    def applyAOstar(self):
        self.aoStar(self.start, False)
    def getNeighbors(self,v):
        return self.graph.get(v,'')
    def getStatus(self,v):
        return self.status.get(v,0)
    def getHeuristicNodeValue(self,h):
        return self.H.get(h,0)
    def setStatus(self,v,val):
        self.status[v]=val
    def setHeuristicNode(self,h,val):
        self.H[h]=val
    def printSolution(self):
        print(self.start)
        print(self.solutionGraph)
    def computeMinCost(self,v):
        minCost=0
        costToChildNodeList={}
        costToChildNodeList[minCost]={}
        flag=True
        for childTuple in self.getNeighbors(v):
            cost=0
            nodeList=[]
            for c,weight in childTuple:
                cost+=self.getHeuristicNodeValue(c)+weight
                nodeList.append(c)
            if flag==True:
                minCost=cost
                costToChildNodeList[minCost]=nodeList
                flag=False
            else:
                if minCost>cost:
                    minCost=cost
                    costToChildNodeList[minCost]=nodeList
        return minCost,costToChildNodeList[minCost]
    def aoStar(self,v,backtracking):
        print(self.H)
        print(self.solutionGraph)
        print(v)
        
        if self.getStatus(v)>=0:
            minCost,childListNode=self.computeMinCost(v)
            self.setStatus(v, len(childListNode))
            self.setHeuristicNode(v, minCost)
            solved= True
            for childNode in childListNode:
                self.parent[childNode]=v
                if self.getStatus(childNode)!=-1:
                    solved= solved & False
            if solved==True:
                self.setStatus(v, -1)
                self.solutionGraph[v]=childListNode
            if v!=self.start:
                self.aoStar(self.parent[v],True)
            if backtracking==False:
                for childNode in childListNode:
                    self.setStatus(childNode, 0)
                    self.aoStar(childNode, False)
h1={'A':1,'B':6,'C':2,'D':12,'E':2,'F':1,'G':5,'H':7,'I':7,'J':1}
graph1={
        'A':[[('B',1),('C',1)],[('D',1)]],
        'B':[[('G',1),('H',1)]],
        'C':[[('J',1)]],
        'D':[[('E',1),('F',1)]],
        'G':[[('I',1)]]
}
G1=Graph()
G1._init_(graph1,h1,'A')
G1.applyAOstar()
G1.printSolution()