### Exercise 10.12: find interlock pairs in the word list
# s h o e + c o l d -> schooled

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

# **a better approach** : from the output to solve the input -> avoids double loop!
   # also avoids the problem of non-equal length input words
def interlock(wordlist, word):
    """checks whether a word contains"""
    evens = word[::2]
    odds = word[1::2]
    return evens in wordlist and odds in wordlist


def make_word_dict():
    word_dict = {}
    with open('words.txt') as f:
        for line in f:
            word = line.strip().lower()
            word_dict[word] = None
    return word_dict

worddict = make_word_dict()

# this approach is much faster!
# for word in worddict:
#     if interlock(worddict, word):
#         print(word, word[::2], word[1::2])


def interlock_general(worddict, word, n=3):
    """checks whether a word contains n interleaved words
    wordlist: dictionary of strings
    word: string
    n: number of interleaved words
    """
    wl = []
    for i in range(n):
        w = word[i::n]
        wl.append(w)
    for w in wl:
        if w not in worddict: return False
    return True
## simpler version, saves 3 lines and 1 loop:
    # for i in range(n):
    #     w = word[i::n]
    #     if w not in worddict: return False
    # return True


for word in worddict:
    if interlock_general(worddict, word, 4):
        print(word, word[::4], word[1::4], word[2::4], word[3::4])




## initial try, works, but very slow..
# def interlock_pairs(w1, w2, wl): # also + (w2, w1, wl)
#     # for :
#     interlocked1 = interlock_output(w1, w2)
#     interlocked2 = interlock_output(w2, w1)
#     if interlocked1 in wl:
#         print(w1, w2, interlocked1)
#     if interlocked2 in wl:
#         print(w2, w1, interlocked2)


# for w1 in worddict:
#     for w2 in worddict:
#         if len(w2) == len(w1):
#             interlock_pairs(w1, w2, worddict)

