from struct import *

fname = r"test.txt"
fomt = "10s7i"

#pkd = Struct(fomt)
pkd = pack(fomt,b'this is a test',12345,1,2,2,3,3,5)
print(pkd)

with open(fname, "bw") as fp:
    fp.write(pkd)
    
with open(fname,"br") as fp:
    pkd2 = fp.read()
upkd = unpack(fomt, pkd2)
print(upkd)
