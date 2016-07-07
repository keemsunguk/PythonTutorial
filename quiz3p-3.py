def interleave(s1, s2):
    s1length = len(s1)
    s2length = len(s2)
    endNo = min(s1length, s2length)
    
    resString = ""
    ii = 0
    for i in range(endNo):
        resString += (s1[i]+s2[i])
        ii += 1
    
    if(s1length > s2length):
        resString += s1[ii:]
    elif(s1length < s2length):
        resString += s2[ii:]
    return resString # replace with your answer!

def testInterleave():
    print("Testing interleave()...", end="")
    assert(interleave("abcdefg", "abcdefg") == "aabbccddeeffgg")
    assert(interleave("abcde", "abcdefgh") == "aabbccddeefgh")
    assert(interleave("abcdefgh","abcde") == "aabbccddeefgh")
    assert(interleave("Smlksgeneg n a!", "a ie re gsadhm") ==
                      "Sam likes green eggs and ham!")
    assert(interleave("","") == "")
    print("Passed!")

testInterleave()