# 加\可以去掉第一行表头，不加就会默认有表头
s = '''\
1,tom,20,
2,jerry,16,
3,,,
'''

with open('e:/test1.csv', 'w') as f:
    # f.writelines(s.splitlines())
    for line in s.splitlines():
        f.write(line + '\n')



# ~~~~~~~~~~~~~~~~~~~

from pathlib import Path

p = Path('e:/tmp/mycsv/test.csv')
parent = p.parent
if not parent.exists():
    parent.mkdir(parents=True)

csv_body = '''\
id,name,age,comment
1,zs,18,"I'm 18"
2,ls,20,"this is a ""test"" string."
3,ww,23,"中国

国庆
"
'''
p.write_text(csv_body)


# ~~~~~~~~~~~~~~~~~~
from pathlib import Path
import csv

# csv.reader
# csv.writer


path = 'e:/csv/test.csv'
p = Path(path)
if not p.parent.exists():
    p.parent.mkdir(parents=True)

line = [1, "tom", 20]
with open('path', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(line)



