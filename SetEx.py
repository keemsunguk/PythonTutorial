#Set Example
s = set("wahoo")
print(s)     # surprised?


s = { 2, 3, 5 }
print(s)    # prints { 2, 3, 5 }

s = set([2,4,8])
print(s)          # prints {8, 2, 4} in standard Python (though not in brython)
for element in s: # prints 8, 2, 4
    print(element)
    
# 0. Preliminaries
import time
n = 1000

# 1. Create a list [2,4,6,...,n] then check for membership
# among [1,2,3,...,n] in that list.

# don't count the list creation in the timing
a = list(range(2,n+1,2))

print("Using a list... ", end="")
start = time.time()
count = 0
for x in range(n+1):
    if x in a:
        count += 1
end = time.time()
elapsed1 = end - start
print("count=", count," and time = %0.4f seconds" % elapsed1)

# 2. Repeat, using a set
print("Using a set.... ", end="")
start = time.time()
s = set(a)
count = 0
for x in range(n+1):
    if x in s:
        count += 1
end = time.time()
elapsed2 = end - start
print("count=", count," and time = %0.4f seconds" % elapsed2)
print("With n=%d, sets ran about %0.1f times faster than lists!" %
      (n, elapsed1/elapsed2))
print("Try a larger n to see an even greater savings!")

# in
s = { 1, 2, 3 }
print(0 in s)
print(1 in s)
#x not in s	test x for non-membership in s	
s = { 1, 2, 3 }
print(0 not in s)
print(1 not in s)
#s.add(x)	add element x to set s	
s = { 1, 2, 3 }
print(s, 4 in s)
s.add(4)
print(s, 4 in s)
#s.remove(x)	remove x from set s; raises KeyError if not present	
s = { 1, 2, 3 }
print(s, 3 in s)
s.remove(3)
print(s, 3 in s)
#s.remove(3) # crashes
#s.discard(x)	removes x from set s if present	
s = { 1, 2, 3 }
print(s, 3 in s)
s.discard(3)
print(s, 3 in s)
s.discard(3) # does not crash!
print(s, 3 in s)