### Exercise 11.6: solving the homophone problem
# looking for words that are homophones when removed of the first & second letter


from pronounce import read_dictionary

pron_dict = read_dictionary("/Users/sinansmac/Documents/MIT600/c07b.txt")


def homophone(word):
    """Checks to see if the word has the following property:
    removing the first letter yields a word with the same
    pronunciation, and removing the second letter yields a word
    with the same pronunciation.

    word: string
    """
    global pron_dict
    word1 = word[1:]
    word2 = word[0] + word[2:]
    # if word in pron_dict:
    val = pron_dict[word]
    if word1 not in pron_dict or word2 not in pron_dict: return False
    return val == pron_dict[word1] and val == pron_dict[word2]

if __name__ == '__main__':
    for word in pron_dict:
        if homophone(word):
            print(word, word[1:], word[0]+word[2:])

# compared to Allen's version, mine is much simpler, as I don't check for words.txt
# words are recognised as legitimate if they can be found in pron_dict
# (not always true in a linguistic sense, but we dont lose any valid words)