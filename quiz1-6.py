import math

def fabricExcess(fabricInches):
    newNo = fabricInches - int(fabricInches / 36)*36
    
    if newNo == 0:
        newNo = 0
    else:
        newNo = 36-newNo
    return newNo # replace with your solution

def almostEqual(d1, d2):
    epsilon = 0.00001
    return abs(d1-d2) <= epsilon

def testFabricExcess():
    print("Testing fabricExcess()...", end="")
    assert(fabricExcess(0) == 0)
    assert(fabricExcess(1) == 35)
    assert(fabricExcess(35) == 1)
    assert(fabricExcess(36) == 0)
    assert(fabricExcess(37) == 35)
    # use almostEqual when comparing floats
    assert(almostEqual(fabricExcess(35.5), 0.5))
    assert(almostEqual(fabricExcess(36.5), 35.5))
    print("Passed.")

testFabricExcess()