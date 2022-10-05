#  10/4 eventually this will find strong numbers
#  start small
# create a list of primes up to the largest strong number we are checking for

# makes a list of prime numbers up to the target to use in comparisons  
def makePrimeList(maxNum):
    for x in range(2,maxNum):
        if(testPrime(x)):
            primeList.append(x)

#  tests to see if a specific number is prime returns true if so  used by makePrimeList
def testPrime(testNum):
    for x in range(2, testNum):
         if testNum%x ==0:
            return False
    return True
# takes a number as input and returns a list of its prime factors used by putInList
def primeFactorsOf(evalNum):
    factorList =[]
    for j in primeList:
       if evalNum>j:
           if evalNum%j==0:
                factorList.append(j)
    return factorList

# takes in the highest number to put in the list of primesFactors
#creates a dictionary entry for each one,  and returns the list
def putInList(topNumber):
    myTempList=[]
    for x in range(1,topNumber):
        putIn_Dictionary={
            "Number":x,
            "Prime_Factors":primeFactorsOf(x)
        }
        myTempList.append(putIn_Dictionary)
    return myTempList

# called addStrong because it is adding the strong t/f  key value pair to each dictionary       
def addStrong(theList):
    for aDict in theList: 
        theList=aDict["Prime_Factors"] 
        theNumber=aDict["Number"]
        isStrong =True
        if len(theList) >0:
            for y in range (0,len(theList)):
                if theNumber%(theList[y] * theList[y])!=0:
                    isStrong=False
                    aDict["Strong"]=False  
        else:  #  if the list is to short
            isStrong=False
            aDict["Strong"]=False 
        if( isStrong):  
             aDict["Strong"]=True        
                
    
maxStrong =1000
maxStrong+=1
primeList =[]
makePrimeList(maxStrong)
finalNumberList=putInList(maxStrong)
addStrong(finalNumberList)
for element in finalNumberList:
    if element["Strong"]==True:
        print (element)













