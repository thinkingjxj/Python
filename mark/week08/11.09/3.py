import pickle

# 对象序列化
class AA:
    tttt = 'ABC'
    def show(self):
        print('abc')

a = AA()
sr = pickle.dumps(a)
print('sr={}'.format(sr))

a1 = pickle.loads(sr)
print(a1.tttt)

a1.show()


class AAA:
    def __init__(self):
        self.tttt = 'abc'

b = AAA()
sr = pickle.dumps(b)
print('sr={}'.format(sr))

b1 = pickle.loads(sr)
print(b1.tttt)

# 定义类AAA，并序列化到文件
# 实验
class AAA:
    def __init__(self):
        self.tttt = 'abc'
aaa = AAA()
sr = pickle.dumps(aaa)
print(len(sr))

# file = 'e:/'
# with open(file, 'wb') as f:
#     pickle.dump(aaa, f)
