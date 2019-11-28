import pandas as pd
import numpy as np

#function that reads lines of file and converts to list of strings
def getFile(fFileName):
    fFileName = "/Users/robertscott/OneDrive - University of Birmingham/Python/" + fFileName + ".txt"

    #initialise string text array to read in to. 
    stringArray = []

    #read each line from a text file, and strip linebreaks
    with open(fFileName) as f:
        lines = f.readlines()
        for line in lines:
            #strip line breaks
            stringArray.append(line.rstrip())
            
    return(stringArray)

#first iteration of BWT
def bwt(fInput):
    #create an array of size n.n where n is the length of the string
    fInput =  '$' + fInput 
    stringLen = len(fInput)
    #fill with blank
    transformArray = np.full((stringLen, stringLen), '')

    #where i is row and j is column, fill with string
    for i in range(stringLen):
        for j in range(stringLen):
            transformArray[i, j] = fInput[j]
        transformArray[i] = np.roll(transformArray[i], i)

    #create panda dataframe from numpy array.
    stringDataFrame = pd.DataFrame(transformArray)
    #create a list of the indices of the dataframe
    templist = list(range(stringLen))
    sorted_dataFrame = stringDataFrame.sort_values(by = templist)
    sorted_dataFrame = sorted_dataFrame.reset_index()

    lastCol = sorted_dataFrame[len(sorted_dataFrame)-1]
    revString = ''
    for i in range(len(sorted_dataFrame)):
        revString += lastCol[i]
    return(revString)

#improved iteration of BWT
def improvedBWT(fInput):
    fInput = '$' + fInput
    table = []
    for i in range(len(fInput)):
        table.append(fInput[i:] + fInput[:i])
    table = sorted(table)
    lastCol = [row[-1:] for row in table]
    return(lastCol)