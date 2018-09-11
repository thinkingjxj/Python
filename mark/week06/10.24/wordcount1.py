# 第一次处理
# os.path. /usr/local/lib '/usr/local/lib']) 3.2: os.path.islink(path)
# pathname.  islink() $name os.stat_float_times() ~user e.g.  /dir  (such
# 第二次处理
# c:foo usr/local/lib os.path os.path.splitdrive(path 3.2 start=os.curdir
# os.path.supports_unicode_filenames    .   +  -


def wordcount(file='sample.txt'):
    chars = '''~!@#$%^&*()_+{}[]|\\/"'=;:.<>,_'''
    charset = set(chars)
    with open(file, encoding='utf-8') as f:
        word_count = {}
        for line in f:
            # print(i, line)
            words = line.split()

            for k in words:
            #for k, v in zip(words, (1,) * len(words)):
                k = k.strip(chars)
                if len(k) < 1:
                    continue
                k = k.lower()
                start = 0
                for i, c in enumerate(k):
                    if c in charset:  # c:foo abc 3.5.3  lib/posixpath.py a///b
                        # print(k[start:i],start,i)
                        if start == i:
                            start = i + 1
                            continue
                        key = k[start:i]
                        word_count[key] = word_count.get(key, 0) + 1
                        start = i + 1
                else:
                    # print('~~~',k[start:])
                    key = k[start:]
                    word_count[key] = word_count.get(key, 0) + 1
                print()

    lst = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for i in range(10):
        if i < len(lst):
            print(str(lst[i]).strip("'()").replace("'", ""))

    return lst


wc = wordcount()
print(wc)
print(len(wc))


# path, 137
# the, 136
# is, 60
# a, 59
# os, 50
# if, 43
# and, 40
# to, 34
# of, 33
# on, 33

for k, v in wc:
    if k.find('path') > -1:
        print(k, v)
