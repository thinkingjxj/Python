import re
from collections import defaultdict

regex = re.compile('[^\w+]')

def wordcount(path):
    d = defaultdict(lambda :0)
    with open('C:/\\Users\\10649\\Desktop\\sample.txt', encoding='utf8') as f:
        for line in f:
            for x in regex.split(line):
                if len(x) >= 1:
                    d[x.lower()] += 1
    return d

i = 0
for x in sorted(wordcount('sample.txt').items(), key=lambda x:x[1], reverse=True):
    if i < 10:
        print(x)
    i += 1



# d = defaultdict(lambda :0)
#
# with open('C:/\\Users\\10649\\Desktop\\sample.txt', encoding='utf8') as f:
#     for line in f:
#         for x in regex.split(line):
#             if len(x) >= 1:
#                 d[x.lower()] += 1
# print(d)