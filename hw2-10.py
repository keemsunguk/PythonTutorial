


print ("use bisection to approximate x where x**5 == 2**x")

def f3(x): return x**5 - 2**x # f(1)<0, f(2)>0

def findZeroWithBisection(f, x1, x2, ep):
    y1 = f(x1)
    y2 = f(x2)

    if abs(y1) < ep: # save time if x1 is a root
        return x1
    elif abs(y2) < ep: # save time if x2 is a root
        return x2
    elif y1*y2 > 0:
        return None
        
    ymid = 1
    while( abs(ymid) > ep ):
        xmid = (x1+x2)/2
        ymid = f(xmid)
        if(y1*ymid < 0):
            x2 = xmid
        elif(y2*ymid < 0):
            x1 = xmid
        else:
            return None
        
        y1 = f(x1)
        y2 = f(x2)
    return xmid

x = findZeroWithBisection(f3, 1, 2, 0.000000001)
print (" x =", x)                              # prints x = 1.17727855081
print (" check: x**5 - 2**x =", (x**5 - 2**x)) # prints check: x**5 - 2**x = 3.63570817896e-09 

print ("use bisection to approximate phi (the golden ratio):")
def f2(x): return x**2 - (x + 1) # root at x=phi
x = findZeroWithBisection(f2, 0, 2, 0.000000001)
print (" x =", x)                  # prints x = 1.61803398887
phi = (1 + 5**0.5)/2             # the actual value (to within Python's floating point accuracy)
print (" check: x/phi =", (x/phi)) # prints check: check: x/phi = 1.00000000007 (nice!)
