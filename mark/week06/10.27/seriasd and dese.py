import pickle

file = 'e:/ser'
with open(file, 'wb') as f:
    s1 = 99
    s2 = 'abc'
    s3 = ['a', 'b', ['c', 'd']]

    pickle.dump(s2, f)    # dump对象序列化到文件对象，就是存入文件（二进制）；load对象反序列化，从文件读取数据
    pickle.dump(s1, f)    # dumps对象序列化（内存中）   loads对象反序列化
    pickle.dump(s3, f)    # 序列化转换成文件


with open(file, 'rb') as f:
    s = []
    for i in range(3):
        s.append(pickle.load(f))

    print(s)


#对象序列化
class AA:        # AA为此模块下的类
    ttt = 'ABC'
    def show(self):    # show为此类下的方法
        print('abc')

a1 = AA()     # 实例化

sr = pickle.dumps(a1)
print('sr = {}'.format(sr))

a2 = pickle.loads(sr)
print(a2.ttt)
a2.show()

# 上面的例子中，其实就保存了一个类名，因为所有的其他东西都是类定义的东西，是不变的，
# 所以只序列化一个AA类名。反序列化的时候找到类就可以恢复一个对象


class AAA:
    def __init__(self):
        self.tttt = 'abc'

b1 = AAA()
sr = pickle.dumps(b1)
print('sr = {}'.format(sr))

b2 = pickle.loads(sr)
print(b2.tttt)

# 可以看出这回保存了AAA、tttt和abc，因为这才是每一个对象每次都变化的。但是，反序列化的时候
# 要找到AAA类的定义，才能成功。否则就会抛异常
# 可以这样理解：反序列化的时候，类是模子，二进制序列就是铁水

# 应用：
# 本地序列化的情况，应用较少。一般来说，大多数场景都应用在网络中。将数据序列化后通过网络传输到远程节点，
# 远程服务器上的服务将接收到的数据反序列化后，就可以使用了
# 但是，要注意一点，远程接收端，反序列化时必须有对应的数据类型，否则就会报错，尤其是自定义类，必须远程得有

class AAA:
    def __init__(self):
        self.tttt = 'abc'

aaa = AAA()
sr = pickle.dumps(aaa)
print(len(sr))


f = 'e:/ser'
with open(file, 'wb') as f:
    pickle.dump(aaa, f)

