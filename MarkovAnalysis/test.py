import string

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

print('total number of words:', total_words(hist))
print('Number of different words:', different_words(hist))

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

print_most_common(hist, 20)