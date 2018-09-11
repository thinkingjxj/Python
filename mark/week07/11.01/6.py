import re

s = '''bottle\nbag\nbig\nable'''

regex = re.compile('(b(?P<body>\w+)(?P<tail>e))')

matcher = regex.search(s)
# matcher = regex.findall(s)
print(matcher)
print(matcher.groups())
print(matcher.group(0))
print(matcher.group(1))
print(matcher.group(2))
print(matcher.group(3))



matcher = regex.finditer(s)
print(matcher)
for x in matcher:
    print(x)
    print(x.groups())
    print(x.group(0))
    print(x.group(1))
    print(x.group(2))
    print(x.group(3))
    print(x.groupdict())
    print('----------')