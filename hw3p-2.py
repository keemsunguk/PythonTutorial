import string

def wordWrap(s, n):
    res = ""
    
    for i in range(0,len(s),n):
        print(i, s[i:i+n])
        res += s[i:i+n]
        res +="\n"
        
    return res[:len(res)-1]


def testWordWrap():
    assert(wordWrap("abcdefghij", 4)  ==  """\
abcd
efgh
ij""")
    assert(wordWrap("a b c de fg",  4)  ==  """\
a-b
c-de
fg""")

    print("Passed...")
    

testWordWrap()
