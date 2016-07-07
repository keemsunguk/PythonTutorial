import math

def kthPositiveDigit(n, k):
    upper = (n//(10**(k+1)))*(10**(k+1))
    res = (n-upper)//(10**k)
    return res 

def isHappyNumber(n):
    x = n  #copy to local variable
    
    if x < 1:
        return False
    else:
        while x > 9:
            endNo = int(math.log10(x))
            sumsq = 0
            for i in range(endNo+1):
                sumsq += kthPositiveDigit(x,i)**2
                
            x = sumsq
            
        if (x == 1) or (x == 7):
            return True
        else:
            return False


def testHappyNumber():    
    assert(isHappyNumber(-7) == False)
    assert(isHappyNumber(1) == True)
    assert(isHappyNumber(2) == False)
    assert(isHappyNumber(97) == True)
    assert(isHappyNumber(98) == False)
    assert(isHappyNumber(404) == True)
    assert(isHappyNumber(405) == False)
    print("Passed")
    
testHappyNumber()