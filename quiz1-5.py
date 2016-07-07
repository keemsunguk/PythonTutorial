def isPerfectSquare(n):
    if n < 0:
        return False
        
    if int(n**0.5) == n**0.5:
        return True
    else:
        return False # replace with your solution

def testIsPerfectSquare():
    print("Testing isPerfectSquare...", end="")
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(32) == False)
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(-16) == False)
    print("Passed!")

testIsPerfectSquare()