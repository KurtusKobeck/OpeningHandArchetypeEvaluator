import math
import time

#The goal of this sim:
#Determine the odds of a keepable opening hand

class InvalidInput(Exception):
    #exists to give functionality to the custom exception in question
    def __init__(self,*args):
        if args:
            self.message=args[0]
        else:
            self.message=None
    def __str__(self):
        if self.message:
            return 'InvalidInput, {0} '.format(self.message)
        else:
            return "Invalid Input has been raised!"
        
def nChooseA(n,a):
    #Returns the number of possible combinations when 'a' objects are selected from 'n' objects without replacement.
    #Example:
    #print(str(nChooseA(333,67))+" possible cominations")
    startTimeNchooseA=time.time()
    m=math.factorial(n)/(math.factorial(n-a)*math.factorial(a))
    print("Time elapsed on operation (nChooseA): "+str(time.time()-startTimeNchooseA))
    return m


def theseFromThat(pulls,pool):
    #Returns the likelihood of exactly the given pulls from the pool.
    #raises error if the pulls are not present in the pool
    #raises error if pulls is longer than the pool
    #raises error if the quantity of an element within pulls is not present within the pool.
    #Future optimizations: Pulls and pool take the form of "stars and bars" rather than straight lists/arrays.
    #pulls example: "2 2's and a 4" => [[2,2],[4,1]], [[target value, # of pulls desired],[...]...]
    #Example: print(str(theseFromThat([[0,1]],range(0,100))))
    startTimeTheseFromThat=time.time()
    for pull in pulls:
        totalOccurencesInPool=pool.count(pull[0])
        if(totalOccurencesInPool<1):
            raise InvalidInput
    numerator=1
    poolLen=len(pool)
    sumOfPulls=0
    for pull in pulls:
        #totalOccurencesInPool=pool.count(pull[0])
        numerator=nChooseA(pool.count(pull[0]),pull[1])*numerator
        sumOfPulls+=pull[1]
    denominator=nChooseA(poolLen,sumOfPulls)
    print("Time elapsed on operation (theseFromThat) {0}: ".format(pulls)+str(time.time()-startTimeTheseFromThat))
    return numerator/denominator

def sumTheOdds(keepableHandDistributions,target):
    #Returns the total odds of drawing at least one of those hands
    #keepableHandDistribution is a list of "pulls", i.e. lists of lists [[thingToBePulled,NumberOfPullsDesired],...]
    #Ex:
    #target is the object to be pulled from
    totalOdds=0
    for pulls in keepableHandDistributions:
        totalOdds+=theseFromThat(pulls,target)
    return totalOdds
startTime=time.time()
deckContents=[]
landCount,rampCount,gasCount=37,13,49
#landCount,rampCount,gasCount=38,16,45
#landCount,rampCount,gasCount=39,17,43
#interactionCount=10
#sweeperCount=3
#tutorCount=2
for i in range(0,99):
    if(i<landCount):
        deckContents.append(0)
    elif(i<landCount+rampCount):
        deckContents.append(1)
    elif(i<landCount+rampCount+gasCount):
        deckContents.append(2)
    else:
        deckContents.append(3)
#print(str(theseFromThat([[0,3],[1,2],[2,2]],deckContents)))
#print("Done! Total Time Spent Running: "+str(time.time()-startTime))
startTime=time.time()
print(str(sumTheOdds([[[0,2],[1,2],[2,3]],[[0,2],[1,3],[2,2]],[[0,2],[1,4],[2,1]],[[0,3],[1,1],[2,3]],[[0,3],[1,2],[2,2]],[[0,3],[1,3],[2,1]],
                      [[0,4],[1,0],[2,3]],[[0,4],[1,1],[2,2]],[[0,4],[1,2],[2,1]],[[0,5],[1,0],[2,2]],[[0,5],[1,1],[2,1]]],deckContents)))
print("Done! Total Time Spent Running: "+str(time.time()-startTime))
