# f = open('C:/\\Users\\10649\\Desktop\\1.txt', 'rb')
# s = f.read()
# f.close()

import re


def count_words(file_path):
    dic = {}
    with open('c:/\\Users\\10649\\Desktop\\1.txt', 'rb') as file:
        text = file.read().decode()
        words = re.findall(r'[a-zA-Z]+', text)
        #re.split('[^-\w]+', 1.text)
        for i in words:
            if i not in dic:
                dic[i] = 1
            dic[i] += 1
        count = len(words)
    return count, dic
print(count_words('1.text'))

for i in sorted(dic.items(), key=lambda x:x[1]):
    if i < 10:
        print(i)


from collections import defaultdict

d = defaultdict()    # 默认初始值value=0

def wdct(f):
    reg = re.split('[^-\w]', 1.txt):
    for sub in reg:
        if len(sub) > 0:
            d[sub] += 1
# 排序











# def count_words(file_path):
#     with open('C:/\\Users\\10649\\Desktop\\1.txt', 'rb') as file:
#         text = file.read().decode()
#         words = re.findall(r'[a-zA-Z]+', text)
#         count = len(words)
#     return count
#
# print(count_words('text.txt'))
