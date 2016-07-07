import string

def areAnagrams(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    res = True
    for i in range(len(s1)):
        if s1.count(s1[i]) != s2.count(s1[i]):
            return False
            
    return res # replace with your answer!

def testAreAnagrams():
    print("Testing areAnagrams()...", end="")
    assert(areAnagrams("", "") == True)
    assert(areAnagrams("abCdabCd", "abcdabcd") == True)
    assert(areAnagrams("abcdaBcD", "AAbbcddc") == True)
    assert(areAnagrams("abcdaabcd", "aabbcddcb") == False)
    print("Passed!")

testAreAnagrams()