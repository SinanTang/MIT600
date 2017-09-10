import string
from itertools import combinations

hand = {'a':1, 'x':2, 'l':3, 'e':1}

subhand_ls2 = []

# for letter in hand:
#     han = hand.copy()
#     for j in range(len(letter)+1):
#             han[letter] = j
#             print(han)
#             if han not in subhand_ls2:
#                     print(subhand_ls2)
#                     subhand_ls2.append(han)
#                     print(subhand_ls2)
#                     print()

# print('final sub list:', subhand_ls2)

handstr = 'aelllxx'


def hand_string(hand):
    str = ''
    for letter in hand:
        for i in range(1, hand[letter]+1):
           str += letter
    str = ''.join(sorted(str))
    return str

# print(hand_string(hand))


def get_frequency_dict(sequence):
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq

def is_sub_string(newS, oldS):
    if len(newS) >  len(oldS): return False
    freq = get_frequency_dict(newS)
    for letter in freq:
        if freq[letter] > hand.get(letter, 0):
            return False
    return True

# print(is_sub_string('aex', handstr))
# print()


subs = []

for i in range(len(handstr)):
    # if handstr[i] not in subs: subs.append(handstr[i])
    # for j in (range(i), range(i+1,len(handstr))):
    for j in range(len(handstr)):
        # for x in j:
        l2 = handstr[i] + handstr[j]
        l2 = ''.join(sorted(l2))
        if is_sub_string(l2, handstr) and l2 not in subs: subs.append(l2)

        for x in range(len(handstr)):
            l3 = l2 + handstr[x]
            # print(l3)  # some are missing
            l3 = ''.join(sorted(l3))
            # print(l3)
            # print()
            if is_sub_string(l3, handstr) and l3 not in subs: subs.append(l3)

# print(len(subs), subs)




# this func cant find all substrings
def sublists():
    subhands = []
    hd = hand.copy()
    for letter in hand:
        # print(letter)
        # while hd[letter] <= hand[letter]:
        for i in range(hand[letter]+1):
            print(i)
            hd[letter] = i
            print(hd)
            hs = hand_string(hd)
            print(hs)
            print()
            if hs not in subhands:
                subhands.append(hs)
    return subhands

# print(len(sublists()), sublists())

def pick_best_word_faster(hand, rearrange_dict):

    combs = []
    handString = hand_string(hand)
    max_len = len(handString)

    for x in reversed(range(1, max_len+1)):
        for y in combinations(handString, x):
            sub = ''.join(y)
            if sub not in combs:
                combs.append(sub)

    best_score = 0
    best_word = ''
    for comb in combs:
        if comb in rearrange_dict:
            word = rearrange_dict[comb]
            points = points_dict[word]
            if points > best_score:
                best_score = points
                best_word = word
    return best_word, best_score



# combs = []
# for x in reversed(range(1, 8)):
#     for y in combinations(handstr, x):
#         sub = ''.join(y)
#         if sub not in combs:
#             combs.append(sub)
#
# print(len(combs), combs)