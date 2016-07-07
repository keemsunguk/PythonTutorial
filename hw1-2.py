def nthFibonacci(n):
    if n == 0:
        res = 1
    elif n < 4:
        res = n
    else:
        res = round(3*1.618**(n-3))
    return res # replace with your solution

def testNthFibonacci():
    print("Testing nthFibonacci()...", end="")
    assert(nthFibonacci(0) == 1)
    assert(nthFibonacci(1) == 1)
    assert(nthFibonacci(2) == 2)
    assert(nthFibonacci(3) == 3)
    assert(nthFibonacci(4) == 5)
    assert(nthFibonacci(5) == 8)
    assert(nthFibonacci(6) == 13)
    print("Passed.")
    print("(Add more tests to be more sure!)")

testNthFibonacci()