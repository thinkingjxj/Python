from pathlib import Path
import csv

p = Path('e:/csv/mycsv/test0.csv')
if not p.parent.exists():
    p.parent.mkdir(parents=True)

line1 = [1, "tom", 20]
line2 = [2, "tom", 20]
line3 = [line1, line2]
with open('path', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(line1)
    writer.writerow(line2)
    writer.writerows(line3)

with open('path') as f:
    reader = csv.reader(f)
    for line in reader:
        if line:
            print(line)
