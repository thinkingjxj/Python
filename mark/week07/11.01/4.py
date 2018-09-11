import re

s = '''os.path([path])'''

print(s.split('.(['))  # 不工作
print(s.split('.'))    # 两段
print(s.split('.['))   # 不工作
print(s.split('(['))


