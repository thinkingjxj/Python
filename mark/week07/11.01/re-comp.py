import re

# re.compile(pattern, flags=0)
# 设定flags，编译模式，返回正则表达式对象regex
# pattern就是正则表达式字符串，flags就是选项。正则表达式需要被编译，为了提高效率，这些编译后的结果被保存，
# 下次使用同样的pattern的时候，就不需要再次编译
# re的其他方法为了提高效率都调用了编译方法，就是为了提速

# re.match(pattern, string,flags=0)
# regex.match(string[,pos[,endpos]])
# match匹配从字符串的开头匹配，regex对象match方法可以重设定开始位置和结束位置。返回match对象

s = '''bottle\nbag\nbig\nable'''
# match方法
print('-----match--------')
# result = re.match('b', s)   # 找到一个就不找了
# print(1, result)    # bottle
# result = re.match('^a', s)  # 没找到，返回None
# print(2, result)
# result = re.match('^a', s, re.M)  # 依然从头开始找，多行模式没有用,,多行模式
# print(3, result)
# result = re.match('^a', s, re.S)  # 依然从头开始找  ，，单行模式
# print(4, result)
# result = re.match('a', s)
# print(5, result)


# 先编译，然后使用正则表达式对象
regex = re.compile('a')
result = regex.match(s)  # 依然从头开始找
print(6, result)
result = regex.match(s, 15)  # 把索引15作为开始，找
print(7, result)   # apple

# search方法
print('---search----')
result = re.search('a', s)
print(8, result)   # apple
regex = re.compile('b')
result = regex.search(s, 1)
print(9, result)  # bag
regex = re.compile('^b', re.M)
result = regex.search(s)
print(10, result)

result = re.fullmatch('bag', s)
print(11, result)
regex = re.compile('bag')
result = re.fullmatch(' ', s)
print(12, result)



