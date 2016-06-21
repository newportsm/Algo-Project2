import sys
import os

#Brute Force or Divide and Conquer Algorithm!
#Total value needs to be < 30 for slow algo to run in a reasonable amount of time
#referenced http://pythonfiddle.com/minimum-coin-brute-force/
def changeslow(array, total):
    
    minCoins = total
    minArr = [0]*len(array)
    
    for i in range(0, len(array)):
        #the coin can be subtracted from the total amount
        if(array[i] <= total):
            
            #subtracting that coin from the total
            currentArr, currentCoins = changeslow(array, total - array[i])
            #adding to the total count of coins
            currentCoins = currentCoins + 1
            #adding to the specific index of that coin
            currentArr[i] = currentArr[i] + 1
            
            if currentCoins < minCoins:
                minCoins = currentCoins
                minArr = currentArr
                
    return minArr, minCoins

#Changegreedy algorithm!
def changegreedy(array, total):
    
    i = len(array) - 1
    currentTotal = total
    countArr = [0] * len(array)
    totalCount = 0
    
    while (currentTotal > 0):
        if(array[i] <= currentTotal):
            currentTotal = currentTotal - array[i]
            countArr[i] = countArr[i] + 1
            totalCount = totalCount + 1
            
        else:
            i = i - 1
    
    return countArr, totalCount

#Dynamic Programming Algorithm!
#Referenced from http://interactivepython.org/runestone/static/pythonds/Recursion/DynamicProgramming.html
def changedp(array, total):
    #to create table from scratch
    minCoinsUsed = [0]*(total + 1)
    minCoinCount = [0]*(total + 1)
    
    #loop through each coin
    for coins in range(total + 1):
        coinCount = coins
        latestCoin = 1
        
        for i in [coinDp for coinDp in array if coinDp <= coins]:
            if(minCoinCount[coins - i] + 1 < coinCount):
                coinCount = minCoinCount[coins - i] + 1
                latestCoin = i
        minCoinCount[coins] = coinCount
        minCoinsUsed[coins] = latestCoin
    
    #parse the table
    minCount = minCoinCount[total]
    minUsed = []
    
    for each in array:
        minUsed.append(0)
    changeIter = total
    
    while changeIter > 0:
        coin = minCoinsUsed[changeIter]
        k = 0
        for j in array:
            if (coin == j):
                minUsed[k] += 1
            k += 1
        
        changeIter = changeIter - coin
        
    return minUsed, minCount

#main function
def main():
    
    #make sure correct number of arguments
    if (len(sys.argv) == 2):
        
        #grab the filename 
        fileName = sys.argv[1]
        inputFile = fileName + ".txt"
        #will append change to the end of input filename and have that be the change results file
        outputFile = fileName + "change.txt"
        
        #file check
        fileCheck = os.path.isfile(inputFile)
        #if no file is found then print out error
        if (fileCheck == False):
            print ("Error: " + inputFile + " not found.")
            return 1
        
        #check to make sure that file exists then notify that algorithms are running
        print("File successfully found, program running!")
        
        #create change results file if it doesn't exist already
        with open(outputFile, 'wt') as changeFile:
            
            #open original file to grab values from
            with open(inputFile, 'rt') as coinFile:
                
                #to hold data
                row = coinFile.read().splitlines()
                
                #tempArray[0] (first line)
                tempArray = 0
                #tempTotal[1] (second line)
                tempTotal = 1
                
                #to list file name at top of results file as required:
                changeFile.write(str(inputFile) + ":\n\n")
                
                #while loop to process rows
                while (tempArray < len(row)):
                    #varibale to toss to function
                    curArray = row[tempArray]
                    
                    #take out '[]'
                    curArray = curArray.replace('[', '')
                    curArray = curArray.replace(']', '')
                    
                    #array(list) to pass to functions that holds coin values
                    curArray = list(map(int, curArray.split(',')))
                    
                    #variable to pass to functions that holds coin value needed
                    curTotal = int(row[tempTotal])
                    
                    #to write original problem to results file
                    changeFile.write("Array of Coin Values: " + str(curArray) + "\n")
                    changeFile.write("Coin Total Needed: " + str(curTotal) + "\n\n")
                    
                    #call to slow function = pass current array and current total
                    resultSlow, slowTotal = changeslow(curArray, curTotal)
                          
                    #to write slow algo results to file
                    changeFile.write("Brute Force Algo:\n")
                    changeFile.write(str(resultSlow) + "\n")
                    changeFile.write(str(slowTotal) + "\n")
                    
                    #call to greedy function - pass current array and current total
                    resultGreedy, greedyTotal = changegreedy(curArray, curTotal)
                    
                    #to write greedy algo results to file
                    changeFile.write("Greedy Algo:\n")
                    changeFile.write(str(resultGreedy) + "\n")
                    changeFile.write(str(greedyTotal) + "\n")
                    
                    #call to dynamic programming algorithm
                    resultDp, dpTotal = changedp(curArray, curTotal)
                    
                    #to write dp algo results to file
                    changeFile.write("Dynamic Programming Algo:\n")
                    changeFile.write(str(resultDp) + "\n")
                    changeFile.write(str(dpTotal) + "\n\n")
                    
                    #to jump to the next correct index in the loop
                    tempArray = tempArray + 2
                    tempTotal = tempTotal + 2
                
                #notify user that program is finished running
                print("Complete. Change results found in " + str(outputFile))
    
    else:
        print("Error: please enter correct number of arguments")
        
main()