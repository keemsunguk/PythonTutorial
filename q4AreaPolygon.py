def areaOfPolygon(L):
    sum = 0
    coord1 = L[0]
    for i in range(1, len(L)):
        coord2 = L[i]
        sum += (coord1[0]*coord2[1]-coord1[1]*coord2[0])
 #       print(coord1[0],"x",coord2[1],"-",coord1[1],"x",coord2[0])
        coord1 = coord2
    coord2 = L[0]    
    sum += (coord1[0]*coord2[1]-coord1[1]*coord2[0])
    return abs(sum)/2
 
def almostEqual(d1, d2):
    epsilon = 10**-8
    return abs(d1 - d2) < epsilon

def testAreaOfPolygon():
    print("Testing areaOfPolygon()...", end="")
    assert(almostEqual(areaOfPolygon([(4,10), (9,7), (11,2), (2,2)]), 45.5))
    assert(almostEqual(areaOfPolygon([(9,7), (11,2), (2,2), (4, 10)]), 45.5))
    assert(almostEqual(areaOfPolygon([(0, 0), (0.5,1), (1,0)]), 0.5))
    assert(almostEqual(areaOfPolygon([(0, 10), (0.5,11), (1,10)]), 0.5))
    assert(almostEqual(areaOfPolygon([(-0.5, 10), (0,-11), (0.5,10)]), 10.5))
    print("Passed!")

testAreaOfPolygon()