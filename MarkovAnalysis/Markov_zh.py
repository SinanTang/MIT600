import random, sys

# import nltk
from nltk.tokenize.stanford_segmenter import StanfordSegmenter

jar = '/Users/sinansmac/Public/StanfordNLP/stanford-segmenter-2017-06-09/stanford-segmenter-3.8.0.jar'
api_jar = '/Users/sinansmac/Public/StanfordNLP/stanford-parser-full-2017-06-09/slf4j-api.jar'
# model = '/Users/sinansmac/Public/StanfordNLP/stanford-segmenter-2017-06-09/data/dict-chris6.ser.gz'

seg = StanfordSegmenter(path_to_jar=jar, path_to_slf4j=api_jar)
seg.default_config('zh')
# sent = u'这是斯坦福中文分词器测试'
# print(seg.segment(sent))


class MarkovZh:
    def __init__(self):
        self.suffix_map = {}
        self.prefix = ()

    def process_file(self, filename, order=1):
        fp = open(filename)
        # self.skip_gutenberg_header(fp)

        for line in fp:
            for word in line.rstrip().split():
                self.process_word(word, order)

    # def skip_gutenberg_header(self, fp):
    #     for line in fp:
    #         if line.startswith('*END*THE SMALL PRINT!'):
    #             break

    def process_word(self, word, order=1):
        if len(self.prefix) < order:
            self.prefix += (word,)
            return
        try:
            self.suffix_map[self.prefix].append(word)
        except KeyError:
            self.suffix_map[self.prefix] = [word]
        self.prefix = self.shift(self.prefix, word)

    def shift(self, t, word):
        return t[1:]+(word,)

    def random_text(self, n=100):
        start = random.choice(list(self.suffix_map.keys()))
        for i in range(n):
            suffixes = self.suffix_map.get(start, None)
            if suffixes == None:
                self.random_text(n-i)
                return
            word = random.choice(suffixes)
            # print(word, end=' ')
            print(word)
            start = self.shift(start, word)



def main(script, filename='chinese_tokens.txt', n=50, order=1):
    try:
        n = int(n)
        order = int(order)
    except ValueError:
        print('Usage: {} filename [# of words] [prefix length]'.format(script))
    else:
        markov = MarkovZh()
        markov.process_file(filename, order)
        markov.random_text(n)


if __name__ == '__main__':
    main(*sys.argv)