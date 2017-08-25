from string import *

# these are some example strings for use in testing your code

#  target strings
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaaggcatggatgtaaatgcag'


# key strings
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
key14 = 'ab'

# print find(target1, key11), find(target1, key11, 6), find(target1, key11, 5)


### Problem 3a: 2 functions to count the number of instances of a string in the target

def countSubStringMatch(target, key):
    counter = []
    for i in range(len(target)):
        match = find(target, key, i)
        try: match == -1
        except: return 0
        # print match
        if match not in counter:
            counter.append(match)
            # print counter
    return len(counter)-1

# print countSubStringMatch(target1, key10), countSubStringMatch(target2, key12), countSubStringMatch(target1, key14)


def countSubStringMatchRecursive(target, key):
    match = find(target, key)
    # match = target.find(key) # for Python 3
    if match == -1:
        return 0 # the base case
    else:
        target = target[match + (len(key) or 1):]
        print target
        return 1 + countSubStringMatchRecursive(target, key)
    # '1+' is essential here, so every recursive cycle can add 1 to the result

# print countSubStringMatchRecursive(target1, key14), countSubStringMatchRecursive(target1, key11)


### Problem 3b: return a tuple of the starting points of matches of the key string in the target string

# 1st solution, doesnt work well
def subStringMatchExact0(target, key):
    # matches = ()
    match = find(target, key)
    matches = (match,)
    # print match, matches
    if match == -1: return "No match"
    else:
        for i in range(countSubStringMatchRecursive(target, key)):
            index = find(target[match + (len(key) or 1):], key)
            match = index
            matches = matches + (index,)
            # print match, matches
    return matches

# second solution, works!
def subStringMatchExact(target, key):
    matches = []
    for i in range(len(target)): # BETTER: range(0, len(target)-len(key)+1)

   # another (faster) solution ->
   #  for i in range(0, len(target)-len(key)+1):
   #      if target[i : i+len(key)] == key:
   #          matches.append(i)

        match = find(target, key, i)
        if match not in matches and match != -1 :
            matches.append(match)
    return tuple(matches)

# print subStringMatchExact2(target1, key13)


def testStringMatch():
    for target in [target1, target2]:
        for key in [key10, key11, key12, key13]:
            print "subStringMatchExact", target, key
            print subStringMatchExact(target, key)

# testStringMatch()



### Problem 3c:

def constrainedMatchPair(firstMatch, secondMatch, length):
    startingIndexes = []
    # firstMatch & secondMatch are tuples
    for n in firstMatch:
        for k in secondMatch:
            if n + length + 1 == k:
                startingIndexes.append(n)
    return tuple(startingIndexes)


## the following procedure you will use in Problem 3

def subStringMatchOneSub(key, target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0, len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss + 1:]
        print('breaking key', key, 'into', key1, key2)
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target, key1)
        match2 = subStringMatchExact(target, key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1, match2, len(key1))
        allAnswers = allAnswers + filtered
        # print('match1', match1)
        # print('match2', match2)
        print('possible matches for', key1, key2, 'start at', filtered)
    allAnswers = reduce(lambda a,b: a if b in a else a+(b,), allAnswers, ())
    return allAnswers # this returns every solutions with many duplicates, so I added the lambda function above

# print subStringMatchOneSub(key12, target1)


### Problem 3d: return a tuple that has all the starting points of matches of the key to the target,
    # such that exactly one element of the key is incorrectly matched to the target

def subStringMatchExactlyOneSub(target, key):
    # return indexes found in subStringMatchOneSub(), but not in subStringMatchExact()
    return tuple([item for item in subStringMatchOneSub(key, target) if item not in subStringMatchExact(target, key)])

print subStringMatchExactlyOneSub(target1, key11), "\n", subStringMatchExactlyOneSub(target2, key11)