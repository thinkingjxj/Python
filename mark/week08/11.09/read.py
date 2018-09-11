# 使用空的class语句来产生一个空的命名空间对象
# 一旦我们产生了空类，我们随着时间用赋值类属性来填充它
class rec:pass

pers1 = rec()
pers1.name = 'mel'
pers1.job = 'trainer'
pers1.age = 40

pers2 = rec()
pers2.name = 'vls'
pers2.job = 'writer'
#pers2.age = 45

# 实例实际上是不同的名称空间
print(pers1.name, pers2.name)


class Perosn:
    def __init__(self, name, job):
        self.name = name
        self.job = job
    def info(self):
        return (self.name, self.job)

rec1 = Perosn('mel', 'trainer')
rec2 = Perosn('vls', 'developer')

print(rec1.job, rec2.info())

# 类总是位于模块中，类是模块对象的属性，类和模块都是命名空间，但类对应于语句
# （而不是整个文件），而且支持多个实例，继承以及运算符重载这些OOP概念
# 总之，模块就像是单个的实例类，没有继承，而且模块对应于整个文件的代码
# 类是通过运行class语句创建的，实例是像函数那样调用类来创建的
# 类属性的创建是通过把属性辅助你给类对象实现的，类属性通常是有class语句中的顶层赋值语句而产生的
# 每个在class语句代码区中赋值的变量名，会变成类对象的属性（从计数角度来讲，class语句的作用域会变成类对象的属性
# 的命名空间）不过，也可以于任何引用类对象的地方（在class语句外）对其属性赋值

# 在一个函数定义中，在第一个拥有默认值的参数之后的任何参数，都必须拥有默认值

