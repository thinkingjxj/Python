import re

s = '0123abca'

regex = re.compile('[ab]')   # 编译好，返回正则表达式对象

# matcher = re.match('\d', s)    # 未编译，每次运行都需要重新编译,索引铆钉在0这个位置了
# print(matcher)
# print(type(matcher))
#
# matcher = regex.match(s)      # 编译后使用
# print(type(matcher))
# print(matcher)
# # 第二个matcher：按说应该能找到，但是match匹配要求必须是在开头，相当于：re.compile('^[ab]')，
# # 这就是match不好的地方
# # 改进：编译后的match方法可以指定位置 ：regex.match(s, 3)
# matcher = regex.match(s, 3)   # 可以修改匹配的位置
# print(type(matcher))
# print(matcher)
# matcher = regex.match(s, 4)
# print(matcher)
# # 局限性：必须确切指定匹配的字符的位置，但大多数时候，并不指定其具体位置，所以用另一个方法
# # match只匹配依次，找不到返回None，找到了立即返回
#
# matcher = re.search('[ab]', s)
# print(type(matcher))
# print(matcher)
#
# matcher = regex.search(s)   # 编译后的，从头向后找，找到一个结束，不再向后找了，立即返回
# print(type(matcher))
# print(matcher)
# search也可以指定位置，可以大大减少搜索范围

# 全匹配

matcher = re.fullmatch('\w+', s)
print(type(matcher))
print(matcher)

# matcher = regex.fullmatch(s)
# 编译后的正则没有fullmatch
matcher = regex.findall(s)
print(type(matcher))
print(matcher)

matcher = re.findall('[ab]', s)
print(matcher)
