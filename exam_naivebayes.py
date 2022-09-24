# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 23:55:00 2022

@author: DELL
"""

import time
import random
import math
import csv
def loadCsv(filename):
    lines=csv.reader(open(filename,'r'))
    dataset=list(lines)
    for i in range(len(dataset)):
        dataset[i]=[float(x) for x in dataset[i]]
    return dataset
def splitDataset(dataset,splitRatio):
    trainSize=int(len(dataset)*splitRatio)
    trainSet=[]
    copy=list(dataset)
    while len(trainSet)<trainSize:
        index=random.randrange(len(copy))
        trainSet.append(copy.pop(index))
    return [trainSet,copy]
def seperateByClass(dataset):
    seperated={}
    for i in range(len(dataset)):
        vector=dataset[i]
        if vector[-1] not in seperated:
            seperated[vector[-1]]=[]
            seperated[vector[-1]].append(vector)
    return seperated
def mean(numbers):
    return sum(numbers)/float (len(numbers))
def stdev(numbers):
    avg=mean(numbers)
    #variance=sum([pow(x-avg,2)for x in numbers])/(float(len(numbers)-1))
    #return math.sqrt(variance)
    return 2.0
def summarize(dataset):
    summaries=[(mean(attributes),stdev(attributes))for attributes in zip(*dataset)]
    del summaries[-1]
    return summaries
def summarizeByClass(dataset):
    seperated=seperateByClass(dataset)
    summaries={}
    for classValue,instance in seperated.items():
        summaries[classValue]=summarize(instance)
    return summaries
def calculateProbablity(x,mean,stdev):
    exponent=math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1/(math.sqrt(2*math.pi)*stdev))*exponent
def calculateClassProbablity(summaries,inputVector):
    probablities={}
    for classValue,classSummaries in summaries.items():
        probablities[classValue]=1
        for i in range(len(classSummaries)):
            mean,stdev=classSummaries[i]
            x=inputVector[i]
            probablities[classValue]*=calculateProbablity(x,mean,stdev)
    return probablities
def predict(summaries,inputVector):
    probablities=calculateClassProbablity(summaries, inputVector)
    bestLabel,bestProb=None,-1
    for classValue,probablity in probablities.items():
        if bestProb <probablity or bestLabel is None :
            bestProb=probablity
            bestLabel=classValue
    return probablities
def getPrediction(summaries,testSet):
    prediction=[]
    for i in range(len(testSet)):
        result=predict(summaries,testSet[i])
        prediction.append(result)
    return prediction
def getAccuracy(testSet,predictions):
    correct=0
    for i in range(len(testSet)):
        if testSet[i][-1]== predictions[i]:
            correct+=1
    return (float(correct)/float(len(testSet)))*100.0
def main():
    dataset=loadCsv('NaiveBayesDiabetes.csv')
    testSet=loadCsv('NaiveBayesDiabetes.csv')
    print('training set ,test set'.format(len(dataset),len(testSet)))
    summaries=summarizeByClass(dataset)
    prediction=getPrediction(summaries,testSet)
    accuracy=getAccuracy(testSet,prediction)
    print('s',summaries)
    print('p',prediction)
    print('A',accuracy)
main()    