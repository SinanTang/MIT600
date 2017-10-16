import os, time

from nltk.tokenize.stanford_segmenter import StanfordSegmenter
start = time.time()

jar = '/Users/sinansmac/Public/StanfordNLP/stanford-segmenter-2017-06-09/stanford-segmenter.jar'
api_jar = '/Users/sinansmac/Public/StanfordNLP/stanford-parser-full-2017-06-09/slf4j-api.jar'
# dict = '/Users/sinansmac/Public/StanfordNLP/stanford-segmenter-2017-06-09/data/dict-chris6.ser.gz'

seg = StanfordSegmenter(path_to_jar=jar, path_to_slf4j=api_jar)
seg.default_config('zh')

# sent = u'这是斯坦福中文分词器测试'
# print(seg.segment(sent))

fp = "chinese.txt"
tokenstr = seg.segment_file(fp)
token_ls = list(tokenstr)
print(len(token_ls), '\n', tokenstr, '\n', token_ls)

# with open('chinese_tokens.txt', 'a') as writef:
#     for line in token_ls:
#         writef.write(line.rstrip().split())

# print(tokens, '\n', type(tokens)) # class 'str'

end = time.time()

print("process time:", round(end-start))

