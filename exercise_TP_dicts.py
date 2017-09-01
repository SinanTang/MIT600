### ways to count how many times a letter appears in a given string

# my first solution:
import string

# get 26 letters
alp = string.ascii_lowercase

# a random string
s = 'sdfgqwdaafsdijiqwr'

for letter in alp:
    count = 0
    for i in s:
        if i == letter:
            count += 1
            # print i, count # result doesnt look pretty


# I came up with a better approach:
def count_letter(str, letter):
    count = 0
    for i in str:
        if i == letter:
            count += 1
    if count > 0:
        print (letter, count)

# for letter in alp:
#     count_letter(s, letter)


# using dictionary

def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

# print histogram('there is a bee on the balcony')

# using get() to write the function more concisely
def histogram2(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1  # dict initialisation: d[key] = value !
    return d

# print histogram('there is a bee on the balcony')


# print out histogram
def print_hist(h):
    for key in h:
    # for key in sorted[h]:
        print key, h[key]


# Reverse Lookup (given value, look for key) -> much slower than forward lookup

# returns the first key that maps to the value
def reverse_lookup(d, v):
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('Value does not appear in the dictionary')

hist = {'a': 2, ' ': 6, 'c': 1, 'b': 2, 'e': 5, 'i': 1, 'h': 2, 'l': 1, 'o': 2, 'n': 2, 's': 1, 'r': 1, 't': 2, 'y': 1}
# print reverse_lookup(hist, 8)


# invert a dictionary
def invert_dict0(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse

# print invert_dict0(hist)


# Memos: a previously computed value that is stored for later use is called a memo
known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

# print fibonacci(9), known


### Exercise 11.1: compare the search time of dict and list & bisection search

with open("words.txt") as f:
# check for a shorter words file
    wordlist = [str(next(f)).strip() for i in range(1000)]
# this leave \r\n trailing behind
    # wordlist = f.readlines()
# remove carriage return and newlines
    # wordlist = []
    # for line in f: wordlist.append(line.strip())


def wordDict(wl, s):
    d = dict()
    for word in wl:
        d[word] = 0
    check = s in d
    return check

# print wordDict(wordlist, 'annoy')


# print check # much faster


### Exercise 11.2: use method setdefault() to rewrite invert_dict

def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        # initialises a list when val is not seen, in the same step appends a key to the empty list
        inverse.setdefault(val, []).append(key) # dont need to worry about the return value of setdefault(), because its a list anyway
    return inverse

# print(invert_dict(hist))


### Exercise 11.3: try to memoize the ackermann function

ack_memo = {(0,0):1, (0,1):2, (1,0):2, (1,1):3, (-1,0):None}

# from  Exercise 6.2 The Ackermann function
def ack(m, n):
    if (m,n) in ack_memo: return ack_memo[(m,n)]
    elif m == 0:
        return n+1
    elif m > 0 and n == 0:
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
    else:
        return None

# print(ack(3,5))

# the Ackermann function cant be memoised b/c its a total recursive function

# Allen's version
cache = {}
def ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ackermann(m-1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ackermann(m-1, ackermann(m, n-1))
        return cache[m, n]

# print(ackermann(3,4))
# print(ackermann(3,9)) # maximum recursion depth exceeded


### Exercise 11.4: use dictionary to write a faster, simpler version of has_duplicates

def has_duplicates2(ls):
    d = {}
    for i in ls:
        d[i] = d.get(i, 0) + 1
        if d[i] > 1: return True
        else: pass

# print(has_duplicates2([1,2,3,4,5,1]))
# print(has_duplicates2([1,2,3,3]))


## Exercise 11.5: find all rotate pairs in a wordlist
# this piece still has bugs
def rotate_word(s, i):
    """find the rotated word of original word s by distance of i"""
    for letter in s:
        # this only considers lower-case words
        if ord(letter) + i < 97: index = ord(letter) + i + 26
        elif ord(letter) + i > 122: index = ord(letter) + i - 26
        else: index = ord(letter) + i

        newLetter = chr(int(index))  # boundary of alphabet: 97 - 122
        # print newLetter
        s = s.replace(letter, newLetter)
    return s

print(rotate_word('melon', 1), rotate_word('melon', 2)) #, rotate_word('melon', -1), rotate_word('hal', 1))

# 1. create a function to test whether two words are rotate-words
# 2. for every word in the wordlist, test whether there is any other word that fulfill the rotate function
# 3. output can be a dict {word:rotate, word:rotate,}

def is_rotate_pair(m, n): # problem of this function: must feed two variables in at the same time!
    if not len(m) == len(n): return False
    # exclude the word itself
    if m == n: return False
    for i in range(-25, 26):
        if rotate_word(m, i) == n:
            return True

# print(is_rotate_pair('melon','cubed'), is_rotate_pair('melon','melon'))

# this works with small input data only....
# tested on 1000, works; 10,000, doesnt work
def find_rotate_pairs(wordlist):
    d = {}
    outputDict = {}
    for i in range(len(wordlist)):
    # d = {} # shouldnt declare d here, it gets empty every time the loop starts
        d[i] = wl[i]
        for key in d:
            # print(d, key, i, wl[i]) # useful for debugging
            if is_rotate_pair(d[key], wordlist[i]):
                # print({d[key]: wl[i]})
                outputDict[d[key]] = wordlist[i]
    return outputDict

wl = ['melon','cubed','ibm', 'hal']
wd = {'melon':None, 'cubed':None, 'ibm':None, 'hal':None}
# print(find_rotate_pairs(wl))

def find_rotate_pairs2(word, wordlist):
    for i in range(1, 14):
        rotated = rotate_word(word, i)
        if rotated in wordlist:
            return word, rotated


# Allen's approach
def make_word_dict():
    """Read the words in words.txt and return a dictionary that contains the words as keys"""
    d = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip().lower()
        d[word] = None # make empty values, save space
    return d

output = {}
def rotate_pairs(word, word_dict):
    """prints all words that can be generated by rotating word.
    word: string
    word_dict: dictionary with words as keys
    """
    global output # my modification
    for i in range(1, 14): # range(-24,0) + range(1,25): #this escapes 'back'rotation..; my modification: range(-14,0)+range(1,14)
        rotated = rotate_word(word, i)
        print(rotated)
        if rotated in word_dict:
            output[word] = rotated
            # print(word, i, rotated)

# if __name__ == '__main__':
#     # word_dict = make_word_dict()
#     for word in wd:
#         rotate_pairs(word, wd)
#     print(output)


### Exercise 11.6: solving the homophone problem
# moved to TP_ch11_homophone.py