import re

# s = '''bottle\nbag\nbig\napple'''

# for x in enumerate(s):
#     #print(x[0])    # 代表数字：0-19
#     if x[0] % 8 == 0:
#         print()
#     print(x, end = ' ')
# print('\n')

# print('----match----')
# result = re.match('b', s)
# print(1, result)
# result = re.match('a', s)
# print(2, result)
# result = re.match('^a', s)
# print(3, result)
# result = re.match('^a', s, re.M)
# print(4, result)
# result = re.match('^a', s, re.S)
# print(5, result)
#
# # 先编译，然后使用正则表达式对象
# regex = re.compile('a')
# result = regex.match(s)
# print(6, result)
# result = regex.match(s, 15)
# print(7, result)
#
# print('-----search-----')
# result = re.search('a', s)
# print(8, result)
# regex = re.compile('b')
# result = regex.search(s)
# print(9, result)
# regex = re.compile('^b', re.M)  # 不管是不是多行，找到就返回
# result = regex.search(s)
# print(10, result)
# result = regex.search(s, 8)
# print(11, result)
# # fullmatch方法
# result = re.fullmatch('bag', s)
# print(12, result)
# regex = re.compile('bag')
# result = regex.findall(s)
# print(13, result)

# # findall方法
# result = re.findall('b', s)
# print(1, result)
# regex = re.compile('^b\w+')   # 默认单行模式
# result = regex.findall(s)
# print(2, result)
# regex = re.compile('b\w+')
# result = regex.findall(s)
# print(3, result)
#
# matcher = re.finditer('b', s)
# print(matcher)
# print(next(matcher))
# print(next(matcher))
#
# regex = re.compile('b')
# matcher = regex.finditer(s)
# print(4, matcher)
# print(next(matcher))
# regex = re.compile('b', re.M)
# result = regex.findall(s)
# print(5, result)
# result = regex.finditer(s)
# print(6, result)
# print(next(result))

# re.sub(pattern, repl, string, count=0, flags=0)
# regex.sub(replacement, string, count=0)
# # 使用pattern对字符串string进行匹配，对匹配项使用repl替换
# replacement可以是string、bytes、function、
#
# re.subn(pattern, replabement, string, count=0, flags=0)
# regex.subn(replacement, strint, count=0, falgs=0)
# 同sub返回一个元组(new_string, number_of_subs_made)

# regex = re.compile('b\wg')
# result = regex.sub('magedu', s)
# print(1, result)
# result = regex.sub('magedu', s, 1)
# print(2, result)
#
# regex = re.compile('\s')
# result = regex.subn('\t', s)
# print(3, result)
# result = regex.sub('magedu', s, 1)
# print(4, result)
#
# regex = re.compile('\s+')
# result = regex.subn('\t', s)
# print(5, result)   # 被替换后的字符串及替换次数的元组

# 字符串的分割函数，太难用，不能指定多个字符进行分割
# re.split(pattern, string, maxsplit, flags=0)
# re.split分割字符串

s = '''01 bottle
02 bag
03     big1
100       able'''

# 把每行单词取出来
print(s.split())   # 做不到
result = re.split('[\s\d]+', s)
print(1, result)
regex = re.compile('^[\s\d]+')  # 字符串首
result = regex.split(s)
print(2, result)

regex = re.compile('[\s\d]+', re.M)
result = regex.split(s)
print(3, result)

regex = re.compile('\s+\d+\s+')
result = regex.split(s)
print(4, result)

regex = re.compile('\s+\d+\s+')
result = regex.split(' '+s)
print(5, result)


regex = re.compile('\s+|(?<!\w)\d+')
result = regex.split(s)
print(6, result)
