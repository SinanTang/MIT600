# think python exercises
import random # for 10.8
import time # for 10.9

### Exercise 10.1

t = [[1,2], [3], [4,5,6,7]]

def nested_sum(ls):
    count = 0
    for i in ls:
        count += sum(i)
        # count += reduce(lambda x,y: x+y, i)  # not very intuitive to understand, but works too
    return count

# print nested_sum(t)


### Exercise 10.2 : computes accumulative sum

t2 = [1, 2, 3, 4, 5, 17, 8]

def cumsum(ls):
    new = []
    for i in range(len(ls)):
        new.append(sum(ls[:i+1]))
    return new

# print cumsum(t2)


### Exercise 10.3

def middle(ls):
    a = ls[1:-1]
    return a

# print middle(t2)


### Exercise 10.4

def chop(ls):
    del ls[0] # del ls[0, -1] doesnt work, multi del can only be applied to adjacent elements, eg. [2:5]
    del ls[-1]

# chop(t2)
# print t2


### Exercise 10.5

def is_sorted(ls):
    new = sorted(ls)
    return new == ls

# print is_sorted(['b', 'c', 'c'])


### Exercise 10.6

def is_anagram(s1, s2):
    ls1 = sorted(list(s1))
    ls2 = sorted(list(s2))
    if ls1 == ls2: return True

# print is_anagram('carnew', 'newcar')


### Exercise 10.7

def has_duplicates(ls):
    count = []
    for i in ls:
        if i not in count:
            count.append(i)
        else: return True

# print has_duplicates([1,3,5,2])


### Exercise 10.8: solving birthday paradox (assume 23 students)

def count_same_birthday(num):
    birthdays = []
    counter = 0
    for i in range(num):
        birthday = random.randint(1, 365)
        # print birthday
        if birthday in birthdays:
            counter += 1
            # print counter
        birthdays.append(birthday)
    return counter

# print count_same_birthday(23)

def prob_birthday_coincide_stimulator(num):
    count = 0
    for i in range(1000):  # can change the number of stimulator runs
        c = count_same_birthday(num)
        # increase count by 1 if there is any pair with the same birthday
        if c >= 1:
            count += 1
            print count
    return count/1000.0

# print prob_birthday_coincide_stimulator(30)


### Exercise 10.9

def wordlist1():
    """read lines from a file and builds a list using append."""
    wordlist = []
    f = open('words.txt')#.readlines()
    for line in f:
        wordlist.append(line.strip())
    return wordlist

# wordlist1()

def wordlist2():
    """read lines from a file and builds a list using list + ."""
    wordlist = []
    f = open('words.txt')#.readlines()
    for line in f:
        wordlist = wordlist + [line.strip()]
    return wordlist

# wordlist2()

def elapsed_time(functionName):
    start_time = time.time()
    t = functionName()
    elapsed = time.time() - start_time
    print len(t)
    print t[:10]
    print elapsed, 'seconds'

# elapsed_time(wordlist1)  # < 0.05s, much faster
# elapsed_time(wordlist2)  # > 36s


### Exercise 10.10: binary search for a word in a sorted list

### moved here b/c function in_bisect refernces it
def isPalindrome(s):
    if len(s) <= 1: return True
    else: return s[0] == s[-1] and isPalindrome(s[1:-1])

def ReverseWord(word):
    """output the reverse pair of a given word; need to exclude the palindromes"""
    if isPalindrome(word): return None
    else:
        wl = list(word)
        wl.reverse()
        reversed = ''.join(wl)
    return reversed

# print ReverseWord('car'), ReverseWord('c'), ReverseWord('community')
### a much faster way to get the reverse of a word --> reversed = word[::-1]


def in_bisect(ls, word):
    high = len(ls)
    low = 0
    guess = int((high + low)/2.0) #round() is in danger of causing IndexError, as it can rounds up to the next index
                                  # using 'guess = int(round((high + low)/2.0) -1)' misses a lot of results
    counter = 0
    for i in range(50):
        if word == ls[guess]:
            return True # for exercise 10.11
            # return True if a word is in the list, None otherwise
            # return "Num. of iteration:", str(counter), "; input word is at position", str(guess)
            # the second return is used for exercise 10.10
        elif word > ls[guess]:
            low = guess
        else: high = guess
        guess = int((high + low) / 2.0)
        counter += 1
    return False

## for testing...
def in_bisect2(ls, word):
    high = len(ls)
    low = 0
    guess = int(round((high + low)/2.0) -1) #round() is in danger of causing IndexError, as it can rounds up to the next index
    counter = 0
    for i in range(50):
        if word == ls[guess]:
            return True # for exercise 10.11
            # return True if a word is in the list, None otherwise
            # return "Num. of iteration:", str(counter), "; input word is at position", str(guess)
            # the second return is used for exercise 10.10
        elif word > ls[guess]:
            low = guess
        else: high = guess
        guess = int(round((high + low) / 2.0) -1 )
        counter += 1
    return False

with open('words.txt') as f:
    wordlist = []
    for line in f:
        wordlist.append(line.strip())
    # alternative testing, use smaller input to start with
    # wordlist = [str(next(f)).strip() for x in range(10)]  # xrange() in python 2, range() in python 3

# print in_bisect(wordlist, ReverseWord('acajou'))


### Exercise 10.11: find all the reverse-pairs in the wordlist

# function not used...
def isReverse(w1, w2):
    """find out whether two words are a reverse pair"""
    if len(w1) == len(w2) <= 1 and w1 == w2: return True
    else: return w1[0] == w2[-1] and isReverse(w1[1:-1], w2[1:-1])

# print isReverse('cara', 'arac')


def index_bisect(ls, word):
    """output the index a word in a list, given that we know the word is in it"""
    high = len(ls)
    low = 0
    guess = int((high + low)/2.0)
    counter = 0
    for i in range(50):
        if ReverseWord(word) == ls[guess]:
            return guess
        elif ReverseWord(word) > ls[guess]:
            low = guess
        else: high = guess
        guess = int((high + low) / 2.0)
        counter += 1
    return False

## reverseList should be the correct answer..
reverseList = []

for i in range(len(wordlist)):
    if in_bisect(wordlist, ReverseWord(wordlist[i])):
    # print the reverse pair
        # print wordlist[i], ReverseWord(wordlist[i])
    # print a tuple of the position of the reverse pair found
        reversePair = tuple([i, index_bisect(wordlist, wordlist[i])])
        reverseList.append(reversePair)
    else: pass

# print 'Num. of reverse pair found:', len(reverseList), '\n', 'And their positions in the word list:', reverseList

## for testing...
reverseList2 = []
for i in range(len(wordlist)):
    if in_bisect2(wordlist, ReverseWord(wordlist[i])):
        # print wordlist[i], ReverseWord(wordlist[i])
        reversePair = tuple([i, index_bisect(wordlist, wordlist[i])])
        reverseList2.append(reversePair)
    else: pass

# print 'Num. of reverse pair found:', len(reverseList2), '\n', 'And their positions in the word list:', reverseList2



### Exercise 10.12: find interlock pairs in the word list
# s h o e + c o l d -> schooled
## moved to TP_ch10_interlock.py

def interlock_output(w1, w2):
    """finds all the possible interlock output of a word pair
    w1, w2 : string
    len(w2) == len(w1)
    """
    output = ''
    for i in range(len(w1)):
        output = output + w1[i] + w2[i]
    return output

# print(interlock_output('shoe', 'cold'))



