def kthDigit(n, k):
    if n < 0: 
        n = -1*n
        #print(n)
    res = 0
    upper = (n//(10**(k+1)))*(10**(k+1))
    lower = n-upper
    res = lower//(10**k)
    return res 

def testKthDigit():
    print("Testing kthDigit()...", end="")
    assert(kthDigit(0,0) == 0)
    assert(kthDigit(789, 0) == 9)
    assert(kthDigit(789, 1) == 8)
    assert(kthDigit(789, 2) == 7)
    assert(kthDigit(789, 3) == 0)
    assert(kthDigit(-1234, 3) == 1)
    assert(kthDigit(-3, 1) == 0)
    print("Passed!")

testKthDigit()