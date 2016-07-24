import copy

def removeRowAndCol(A, row, col):
    B = copy.deepcopy(A)
    B.pop(row)
    for i in range(0,len(B)):
#        print(i)
        B[i].pop(col)
    return B

def testRemoveRowAndCol():
    print("Testing removeRowAndCol()...", end="")
    a = [ [ 2, 3, 4, 5],
          [ 8, 7, 6, 5],
          [ 0, 1, 2, 3]]
    assert(removeRowAndCol(a, 1, 2) == [[2, 3, 5], [0, 1, 3]])
    assert(a == [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]])
    assert(removeRowAndCol(a, 0, 0) == [[7, 6, 5], [1, 2, 3]])
    assert(a == [ [ 2, 3, 4, 5],[ 8, 7, 6, 5],[ 0, 1, 2, 3]])
    print("Passed!")

testRemoveRowAndCol()