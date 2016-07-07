import string

def largestNumber(s):
    maxNo = float('-inf')
    for subS in s.split(" "):
        if subS.isdigit():
            thisNo = eval(subS)
            if(thisNo > maxNo):
                maxNo = thisNo

    if maxNo == float('-inf'):
        maxNo = None
        
    return maxNo

def testLargestNumber():
    assert(largestNumber("I saw 3 dogs, 17 cats, and 14 cows!") == 17)
    assert(largestNumber("One person ate two hot dogs!") == None)
    print("Passed")
    
testLargestNumber()