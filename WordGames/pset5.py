# Problem Set 5: 6.00 Word Game
# Time:
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1,
    'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')  # was 'r' in python2.7, gives ValueError in python3.6
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


# print(load_words())

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x, 0) + 1
    return freq


# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def get_word_score(word, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    The score for a word is the sum of the points for letters
    in the word, plus 50 points if all n letters are used on
    the first go.

    Letters are scored as in Scrabble; A is worth 1, B is
    worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string (lowercase letters)
    returns: int >= 0
    """
    # if input word is an empty string
    if len(word) == 0: return 0

    score = 0
    # additional points
    if len(word) == n: score = score + 50

    for letter in word:
        score += SCRABBLE_LETTER_VALUES[letter.lower()]
        # print(score) # for testing
    return score


# print(get_word_score('score', 5))


#
# Make sure you understand how this function works and what it does!
#
def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print(letter, end=' ')  # print all on the same line
    print()  # print an empty line

# display_hand({'a':1, 'c':1, 'i':1, 'h':1, 'm':2, 'z':1})


#
# Make sure you understand how this function works and what it does!
#
def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand = {}
    num_vowels = n // 3

    for i in range(num_vowels):
        x = VOWELS[random.randrange(0, len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1

    for i in range(num_vowels, n):
        x = CONSONANTS[random.randrange(0, len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1

    return hand


#
# Problem #2: Update a hand by removing letters
#
def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    result = {}
    wd = get_frequency_dict(word)
    # print(wd)
    # find the difference between 2 dicts and print it out

    # using set operations
    # first find the unused letters and add to result
    # this operation is permitted in python3.6, not in 2.7
    unused = hand.keys() - wd.keys()
    for letter in unused: result[letter] = hand[letter]

    # then find used letters and add to result
    used = hand.keys() & wd.keys()
    for letter in used:
        if hand[letter] == wd[letter]:
            pass
        else:
            result[letter] = hand[letter] - wd[letter]
    return result

    ## much more concise version:
    # for char in hand:
    # 	result[char] = hand[char] - freq.get(char, 0)
    # return result


# print(update_hand({'a': 1, 'q': 1, 'l': 2, 'm': 1, 'u': 1, 'i': 1}, "quail"))



#
# Problem #3: Test word validity
#
def is_valid_word(word, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.

    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    """
    # check whether word is in wordlist
    if word not in word_list: return False  # "not in wordlist"

    # check whether letters of word are in hand
    wd = get_frequency_dict(word)
    for letter in wd:
        if letter not in hand: return False  # "letter not in hand"
        if wd[letter] > hand[letter]: return False  # "more letters found than hand"

    return True


# word_list = load_words()
# if "aa" in word_list: print("aa is in")

# print(is_valid_word("hello", get_frequency_dict("hello"), word_list))
# print(is_valid_word("rapture", {'r': 1, 'a': 3, 'p': 2, 'e': 1, 't': 1, 'u': 1}, word_list))



#
# Problem #4: Playing a hand
#
def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.

    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, it uses up letters from the hand.

    * After every valid word: the score for that word and the total
      score so far are displayed, the remaining letters in the hand
      are displayed, and the user is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing a single
      period (the string '.') instead of a word.

    * The final score is displayed.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # initialise total score, prepare the loop
    total = 0
    # better method to calculate the total number of letters in a hand
      # should put this outside the loop, b/c rule says 50 additonal points
      # only when all letters are used on the first go
    initial_handlen = sun(hand.values())

    while len(hand) > 0:

        print("Current hand: ", end = ' ')
        display_hand(hand)
        word = input("Enter word, or a . to indicate that you are finished: ")

        # exiting the game
        if word == '.': break

        # check validity
        if not is_valid_word(word, hand, word_list):
            print("Invalid word! Please try again :P")
            continue

        # scoring
        # n = 0
        # for i in hand:
        #     n += hand[i]
        score = get_word_score(word, initial_handlen)
        total += score  # total += score
        print(word, "earned", score, "points. Total:", total, "points")

        hand = update_hand(hand, word)

    return "Total score: " + str(total) + " points."

# word_list = load_words()
# print(play_hand({'a':1, 's':1, 't':2, 'w':1, 'f':1, 'o':1}, word_list))



#
# Problem #5: Playing a game
# Make sure you understand how this code works!
#
def play_game(word_list):
    """
    Allow the user to play an arbitrary number of hands.

    * Asks the user to input 'n' or 'r' or 'e'.

    * If the user inputs 'n', let the user play a new (random) hand.
      When done playing the hand, ask the 'n' or 'e' question again.

    * If the user inputs 'r', let the user play the last hand again.

    * If the user inputs 'e', exit the game.

    * If the user inputs anything else, ask them again.
    """

    # print("play_game not implemented.")  # delete this once you've completed Problem #4
    # play_hand(deal_hand(HAND_SIZE), word_list)  # delete this once you've completed Problem #4

    ## uncomment the following block of code once you've completed Problem #4

    hand = deal_hand(HAND_SIZE) # random init

    while True:
        cmd = input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if cmd == 'n':
            hand = deal_hand(HAND_SIZE)
            play_hand(hand.copy(), word_list)
            print()
        elif cmd == 'r':
            play_hand(hand.copy(), word_list)
            print()
        elif cmd == 'e':
            break
        else:
            print("Invalid command.")




#
# Build data structures used for entire session and play game
#

if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
