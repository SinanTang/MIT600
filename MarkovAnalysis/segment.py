import os,time

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
print(seg.segment_file(fp))

end = time.time()

print("process time:", round(end-start))

