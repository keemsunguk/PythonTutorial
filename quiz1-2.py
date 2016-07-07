def isFactor(f, n):
    if f == 0:
        if n == 0:
            return True
        else:
            return False
    if n/f == n//f:
        return True
    else:
        return False # replace with your solution

def testIsFactor():
    print("Testing isFactor()...", end="")
    assert(isFactor(2, 2))
    assert(isFactor(2, 4))
    assert(not isFactor(2, 5))
    assert(not isFactor(0, 6))
    assert(isFactor(6, 0))
    assert(isFactor(0, 0))
    assert(isFactor(-2, 4))
    print("Passed!")

testIsFactor()