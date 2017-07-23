from string import *

# these are some example strings for use in testing your code

#  target strings
target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'


# key strings
key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'
key14 = 'ab'

# print find(target1, key11), find(target1, key11, 6), find(target1, key11, 5)

### Problem 1: 2 functions to count the number of instances of a string in the target
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

### Problem 2:

### Problem 3:

### the following procedure you will use in Problem 3

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
        print('match1', match1)
        print('match2', match2)
        print('possible matches for', key1, key2, 'start at', filtered)
    return allAnswers
