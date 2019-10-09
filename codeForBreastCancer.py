import csv
import random
import math
import operator

#Function for Importing the the File and read as CSV and load in the DataSet_Training,DataSet_Testing List
def ImportMyDataSet(importingFile, splitConstant, DataSet_Training=[] , DataSet_Testing=[]):
    #Reading the File using the Read mode
    with open(importingFile, 'r') as csvfile:
        #Read the CSV File
        FetchingLines = csv.reader(csvfile)
        #Converting everything to every row as list and load it to dataSet
        IterateRows = list(FetchingLines)
        #Iterate and append it to Training list and Test List
        for row in range(len(IterateRows)-1):
            for col in range(4):
                IterateRows[row][col] = float(IterateRows[row][col])
            if splitConstant > random.random():
                DataSet_Training.append(IterateRows[row])
            else:
                DataSet_Testing.append(IterateRows[row])

# Calculate the Distance between two points using the  Euclidean Distance formula
def calculateDistance(row_one, row_two, length):
    #Initializing the Distance variable to take the distance
    distance_between_two_points = 0
    for row_count in range(length):
        #Use the Formula √(x1-x2)ˆ2 - (y1-y2)ˆ2
        squareValue = pow((float(row_one[row_count]) - float(row_two[row_count])), 2)
        distance_between_two_points = distance_between_two_points + squareValue
    return math.sqrt(distance_between_two_points)


#Predict the nearest class
def findNearestClass(test,k,DataSet_Training):
    # Initialize the list to store the Distance
    distanceList = []
    for x in range(len(DataSet_Training)):
        getDistance = calculateDistance(test, DataSet_Training[x], len(test)-1)
        distanceList.append((DataSet_Training[x], getDistance))
    #Sort the Distances Inorder to find the top K values from the sortedList
    distanceList.sort(key=operator.itemgetter(1))
    #Collecting the K values in the nearestList for the prediction
    nearestList = []
    for row in range(k):
        nearestList.append(distanceList[row][0])
    return nearestList

def getResponse(neighbors):
    rankDict= {}
    for x in range(len(neighbors)):
        response= neighbors[x][-1]
        if response not in rankDict:
            rankDict[response] = 1
        else:
            rankDict[response] +=1
    ranklist = sorted(rankDict.items(), key=operator.itemgetter(1), reverse=True)
    return ranklist[0][0]

def calculateAccuracyPercentage(testSet, predictOutput):
	count = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictOutput[x]:
			count += 1
	return (count/float(len(testSet))) * 100.0

#Main Function
def mainFunction():
    # Here the constant is used for the Randomly pick the Dataset which is later used for the testing.
    splitConstant = 0.70
    # generate predictions
    predictOutput=[]
    #Prepare to pick for testData
    DataSet_Testing=[]
    #Prepare to pick for trainingData
    DataSet_Training=[]
    # First, Implementing the Dataset which is present as a CSV File.
    ImportMyDataSet('Breast_cancer.csv', splitConstant, DataSet_Training, DataSet_Testing)
    #Here K is chosen as '3' inorder to find the 3 nearest points
    k = 3
    for x in range(len(DataSet_Testing)):
        neighbors = findNearestClass(DataSet_Testing[x],k, DataSet_Training)
        # result = predictOutput(neighbors)
        result = getResponse(neighbors)
        predictOutput.append(result)
        print('Prediction', ' actual')
        print('   '+ repr(result) + '       '+repr(DataSet_Testing[x][-1]))
    accuracy = calculateAccuracyPercentage(DataSet_Testing, predictOutput)
    print('Accuracy: ' + repr(accuracy) + '%')

#Calling main method
mainFunction()
