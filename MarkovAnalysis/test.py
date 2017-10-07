import string, random

def file2words(filename):
    # translator = str.maketrans('','', string.punctuation)
    word_dict = {}
    f = open(filename)

    for line in f:
        if line.startswith('*END*THE SMALL PRINT!'):
            break

    wordcount = 0
    for line in f.readlines():
        line = line.replace('-', ' ')
        l = line.split()
        for word in l:
            word = word.lower()
            word = word.strip(string.punctuation + string.whitespace)
            wordcount += 1
            word_dict[word] = word_dict.get(word, 0) + 1

    sorted_wordlist = list(reversed(sorted(word_dict, key=lambda k : word_dict[k])))
    top20 = sorted_wordlist[:20]
    # print(top20)

    return 'Total Wordcount: {}\n\nBook Vocabulary: {}\n\nTop 20 most frequent words: {}' \
           '\n\nFrequency of each word:\n{}'.format(wordcount, len(word_dict), top20, word_dict)


# print(file2words('emma.txt'))


def process_file(filename):
    hist = dict()
    fp = open(filename)
    for line in fp:
        process_line(line, hist)
    return hist

def process_line(line, hist):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()
        hist[word] = hist.get(word, 0) + 1

hist = process_file('emma.txt')

def total_words(hist):
    return sum(hist.values())

def different_words(hist):
    return len(hist)
#
# print('total number of words:', total_words(hist))
# print('Number of different words:', different_words(hist))

def most_common(hist):
    t = []
    for k, v in hist.items():
        t.append((v,k))
    t.sort(reverse=True)
    return t

# t = most_common(hist)
# print('The most common words are:')
# for freq, word in t[:10]:
#     print(word, freq, sep='\t')

def print_most_common(hist, num=10):
    t = most_common(hist)
    print('The most common words are:')
    for freq, word in t[:num]:
        print(word, freq, sep='\t')

# print_most_common(hist, 20)

# look for words in the book that aren't in the word list:
def substract(d1, d2):
    res = {}
    for key in d1:
        if key not in d2:
            res[key] = None
    return res

# words = process_file('words.txt')
# diff = substract(hist,words)


# Exercise 13.6
# def line_to_set(filename):

def set_substract(d1,d2):
    s1 = set(d1)
    s2 = set(d2)
    res = s1.difference(s2)
    return res

# diff_set = set_substract(hist, words)


## random words
# not so efficient algorithm:
def random_word(h):
    t = []
    for word, freq in h.items():
        t.extend([word] * freq)
    return random.choice(t)


# a better algorithm:

def cumulative_freq(freq_list):
    res = []
    for x in range(len(freq_list)):
        cum = 0
        for y in range(x+1):
            cum += freq_list[y]
        res.append(cum)
    return res


def bisearch(ls, num):
    high = len(ls)-1
    low = 0
    guess = (high + low) // 2

    count = 0
    while count < 50:
        if ls[guess] < num and ls[guess+1] > num:
            ans = guess+1
            return ans
        if ls[guess+1] < num:
            low = guess
        if ls[guess+1] > num:
            high = guess
        count += 1
        guess = (high + low) // 2

    return 'iteration exceeds limitation'


def main():
    word_list = list(hist.keys())
    freq_list = list(hist.values())

    cum_ls = cumulative_freq(freq_list)
    tot = sum(hist.values())
    random_num = random.choice(range(1,tot+1))
    index = bisearch(cum_ls, random_num)

    print('random number:', random_num)

    print('guessed index', index)
    print('guessed word:', word_list[index])


if __name__ == '__main__':
    main()