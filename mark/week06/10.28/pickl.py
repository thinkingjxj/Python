from pathlib import Path
import pickle

# 文件序列化和反序列化
file = 'e:/ser'

with open(file,'wb') as f:
    s1 = 99
    s2 = 'abc'
    s3 = ['a', 'b', ['c', 'd']]

    pickle.dump(s1, f)   # 以二进制形式序列化到文件中
    pickle.dump(s2, f)
    pickle.dump(s3, f)

with open(file, 'rb') as f:
    s = []
    for i in range(3):
        s.append(pickle.load(f))    # 反序列化到s中
    print(s)

# 对象序列化
#  class AA:
#      tttt = 'ABC'
#      def show(self):
#          print('abc')

# a1 = AA()  # 实例化
# sr = pickle.dumps(a1)  # 序列化到sr
# print('sr = {}'.format(sr))
#
# a2 = pickle.loads(sr)   # 反序列化到a2
# print(a2.tttt)
# a2.show()


