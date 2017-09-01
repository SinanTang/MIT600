# Problem Set 5: Ghost
# Time:
#

import random

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.

    Depending on the size of the word list, this function may
    take a while to finish.
    """
    # print("Loading word list from file...") # optional
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    # print("  ", len(wordlist), "words loaded.") # optional
    return wordlist


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

# Actually load the dictionary of words and point to it with
# the wordlist variable so that it can be accessed from anywhere
# in the program.

wordlist = load_words()


# function that checks whether a sequence is legitimate
def legitimate_start(word, wordlist):
    """
    check whether the inout word can form the start of a legitimate word.
    :param word: lowercase sequence
    :param wordlist: a long list of legitimate words
    :return: True if word has a legitimate start sequence, False otherwise.
    """
    for i in wordlist:
        if i[:len(word)] == word: return True
    return False

# print(legitimate_start('hel', wordlist), legitimate_start('qz', wordlist))


# function that check whether input is a valid word longer than 3 letters
def longer_than_3(word, wordlist):
    """
    returns True if input word is longer than 3 letters,
    and found in the wordlist
    """
    if len(word) <= 3: return False
    if word in wordlist: return True



# ghost function
def ghost():
    """
    play the interactive word game Ghost between 2 human players.
    :return: which player wins
    """
    print("Welcome to Ghost!"+'\n'+"Player 1 goes first.")
    wordfrag = ''
    print("Current word fragment: {}".format(wordfrag))

    while True:
        init = input("Player 1 says letter: ")
        if init not in string.ascii_letters:
            print("Please enter a valid letter.")
        else: break

    wordfrag = wordfrag + init
    print()

    # 1. loop start
    # while True:
    alternate = [2,1]*5
    for i in range(len(alternate)):
        n = alternate[i]
        players = [1, 2]
        n2 = 0
        for i in players:
            if i != n:
                n2 = i

        print("Current word fragment: ", str(wordfrag))
        # ask for input
        print("Player {}'s turn!".format(n))

        letter = input("Player {} says letter: ".format(n))
        print()

        # check, clean the input
        if letter not in string.ascii_letters:
            print("Please enter a valid letter."+'\n')
            i = i - 1 # not working...
            continue
              ## this step alternates the player, need improving

        letter = letter.lower()

        # add it to wordfrag
        wordfrag = wordfrag + letter

        # conditionals:
        # 1. longer_than_3(word, wordlist);
        if longer_than_3(wordfrag, wordlist):
            print("Player {} loses because {} is a word!".format(n, wordfrag))
            return "Player {} wins!".format(n2)

        # 2. legitimate_start(word, wordlist)
        if not legitimate_start(wordfrag, wordlist):
            print("Player {} loses because no word begins with {}!".format(n, wordfrag))
            return "Player {} wins!".format(n2)

# print(ghost())