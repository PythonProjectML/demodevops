

import numpy as np
import csv
import random
import math
def loadCsv(filename):
    lines=csv.reader(open(filename,'r'))
    dataset=list(lines)
    for i in range(len(dataset)):
        dataset[i]=[float(x)for x in dataset[i]]
    return dataset
def splitRatio(dataset,splitRatio):
    trainSize=int(len(dataset)*splitRatio)
    trainSet=[]
    copy=list(dataset)
    while len(trainSize)<trainSet:
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
def mean(numbers):
    return sum(numbers)/len(numbers)
def stdev(numbers):
    avg=mean(numbers)
    variance=sum([pow(x-avg,2)for x in numbers])/float (len(numbers)-1)
    return math.sqrt(variance)
def summarize(dataset):
    summaries=[(mean(attributes),stdev(attributes))for attributes in zip(*dataset)]
    del summaries[-1]
    return summaries
def summarizeByClass(dataset):
    seperated=seperateByClass(dataset)
    summaries={}
    for classValue,instances in summaries.items():
        summaries[classValue]=summarize(instances)
    return summaries
def calcProbablity(x,mean,stdev):
    exponent=math.exp(-(math.pow(x-mean,2)/(2*math.pow(stdev,2))))
    return (1/(math.sqrt(2*math.pi)*stdev))*exponent
def classcalcProbablity(summaries,inputVector):
    probablities={}
    for classValue,classSummaries in summaries.items():
        probablities[classValue]=1
        for i in range(len(classSummaries)):
            mean,stdev=classSummaries[i]
            x=inputVector[i]
            probablities[classValue]*=calcProbablity(x,mean,stdev)
    return probablities
def predict(summaries,inputVector):
    probablities=classcalcProbablity(summaries,inputVector)
    bestLabel,bestProb=None,-1
    for classValue,probablity in probablities.items():
        if bestLabel is None or bestProb < probablity:
            bestLabel=classValue
            bestProb=probablity
    return bestLabel
def getPrediction(summaries,testSet):
    prediction=[]
    for i in range(len(testSet)):
        result=predict(summaries,testSet[i])
        prediction.append(result)
    return prediction
def getAccuracy(testSet,prediction):
    correct=0
    for i in range(len(testSet)):
        if testSet[i][-1]==prediction[i]:
            correct+=1
    return (float(correct)/(float (len(testSet))))*100.0
def main():
    filename='NaiveBayesDiabetes.csv'
    dataset=loadCsv(filename)
    trainingSet=dataset
    testSet=loadCsv('NaiveBayesDiabetes.csv')
    summarise=summarizeByClass(dataset)
    prediction=getPrediction(summarise,testSet)
    accuracy=getAccuracy(testSet,prediction)
    print(prediction)
    print(accuracy)
main()
