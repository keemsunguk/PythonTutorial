# mastermind.py
# for Recitation 3 (15-110 Spring 2011)

# This program plays Mastermind.  Much more could be added here to
# make gameplay more fun (multiple rounds, scores, etc), but
# it is indeed a playable, if simple, game.  Enjoy!

# This code was written in recitation 3.  It does not have ideal style
# (not many comments, etc), and may even have a bug lurking in it.

################################################
# colorAndPositionMatches
################################################

def colorAndPositionMatches(target, guess):
    # return the number of exact matches (color and position)
    # assumes target and guess are same length
    matches = 0
    for i in range(len(target)):
        if (target[i] == guess[i]):
            matches += 1
    return matches

def testColorAndPositionMatches():
    print ("Testing colorAndPositionMatches()...")
    assert(colorAndPositionMatches("abcde", "bbbbb") == 1)
    assert(colorAndPositionMatches("abcde", "bcdea") == 0)
    assert(colorAndPositionMatches("abcde", "bbbdd") == 2)
    assert(colorAndPositionMatches("abcde", "bbbdd") == 2)
    assert(colorAndPositionMatches("abccc", "cccbb") == 1)
    assert(colorAndPositionMatches("abccc", "acccb") == 3)
    assert(colorAndPositionMatches("qzrmwq", "zzmrqq") == 2)
    print ("Passed!")

################################################
# onlyColorMatches
################################################

def onlyColorMatches(target, guess):
    # return the number of partial matches (color but not position)
    # assumes target and guess are same length
    # also assumes target is composed of lowercase letters
    # First find the total matches (same color, any position)
    totalMatches = 0
    for color in "abcdefghijklmnopqrstuvwxyz":
        targetCount = colorCount(color, target)
        guessCount = colorCount(color, guess)
        totalMatches += min(targetCount, guessCount)
    # Then subtract the exact matces
    partialMatches = totalMatches - colorAndPositionMatches(target, guess)
    return partialMatches

def colorCount(color, target):
    # helper function for onlyColorMatches
    # could be written in one line like so:
    #   return target.count(color)
    # but if we did not know the "count" method (and students are not
    # expected to know it), we could do this:
    count = 0
    for c in target:
        if c == color:
            count += 1
    return count

def testOnlyColorMatches():
    print ("Testing onlyColorMatches()...")
    assert(onlyColorMatches("abcde", "bbbbb") == 0)
    assert(onlyColorMatches("abcde", "bcdea") == 5)
    assert(onlyColorMatches("abcde", "bbbdd") == 0)
    assert(onlyColorMatches("abcde", "bbbdd") == 0)
    assert(onlyColorMatches("abccc", "cccbb") == 3)
    assert(onlyColorMatches("abccc", "acccb") == 2)
    assert(onlyColorMatches("qzrmwq", "zzmrqq") == 3)
    print ("Passed!")

################################################
# getRandomTarget
################################################

# Students are provided the code in this section, and are not
# responsible for understanding getRandomTarget, just using it.

def getRandomTarget(targetSize):
    import time 
    # We can't use Python's random functions until CLEESE 0.11, so
    # we'll use our own pseudorandom numbers
    prime1 = 583621
    prime2 = 329717
    prime3 = 611953
    seed = int(100*time.time()) % prime3
    target = ""
    for i in range(targetSize):
        seed = (((seed * prime1) + (seed * seed * prime2)) % prime3)
        target += chr(ord('a') + (seed % targetSize))
    return target

################################################
# playMastermind
################################################

def playMastermind():
    targetSize = 5  # change to whatever you like
    lastLetter = chr(ord('a') + targetSize - 1)
    print ("---------------------------------")
    print ("Welcome to mastermind!")
    print ("This version uses letters instead of colors.")
    print ("The target contains " + str(targetSize) + " letters.")
    print ("Each letter is between 'a' and '" + lastLetter + "'")
    print ("---------------------------------")
    moves = 0
    target = getRandomTarget(targetSize)
    # of course, the game is more fun if you turn the hint off!
    print ("Hint:  the target is:", target)
    guess = ""
    prompt = "Next guess (" + str(targetSize) + " letters from 'a' to '" + lastLetter + "'): "
    while (target != guess):
        guess = input(prompt)
        if (guess == None):
            # They canceled the input
            print ("Goodbye!")
            return
        elif (len(guess) != targetSize):
            print ("Your guess must have exactly " + str(targetSize) + " characters!")
        else:
            exactMatches = colorAndPositionMatches(target, guess)
            partialMatches = onlyColorMatches(target, guess)
            print ("   Guess:  " + guess,)
            print ("   Exact matches:  ", exactMatches,)
            print ("   Partial matches:", partialMatches)
    print ("You got it!!!!")

def testAll():
    testColorAndPositionMatches()
    testOnlyColorMatches()

testAll()
playMastermind()