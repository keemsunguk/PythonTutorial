import math

def kthPositiveDigit(n, k):
    upper = (n//(10**(k+1)))*(10**(k+1))
    res = (n-upper)//(10**k)
    return res 


def hasConsecutiveDigits(n):
    n = abs(n)
    found = False
    
    if n == 0:
        return False
        
    endNo = int(math.log10(n))
    i = endNo
    
    prev = -1
    curr = kthPositiveDigit(n, endNo)
    
    while i >= 0:
        if prev == curr:
            return True
        else:
            i -= 1
            prev = curr
            curr = kthPositiveDigit(n, i)
        
    return found 

def testHasConsecutiveDigits():
    print("Testing hasConsecutiveDigits()...", end="")
    assert(hasConsecutiveDigits(0) == False)
    assert(hasConsecutiveDigits(123456789) == False)
    assert(hasConsecutiveDigits(1212) == False)
    assert(hasConsecutiveDigits(1212111212) == True)
    assert(hasConsecutiveDigits(33) == True)
    assert(hasConsecutiveDigits(-1212111212) == True)
    print("Passed!")

testHasConsecutiveDigits()