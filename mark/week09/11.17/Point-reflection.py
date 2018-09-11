class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point: ({}, {})".format(self.x, self.y)

    def show(self):
        print(self.x, self.y)

p = Point(4, 5)
print(p)
print(p.__dict__)
p.__dict__['y'] = 16
print(p.__dict__)
p.z = 10           # 动态增加实例的属性
print(p.__dict__)
print(sorted(dir(p)))
print(sorted(p.__dir__()))

# 上例通过属性字典__dict__来访问对象的属性，本质上也是利用的反射能力
# 但是，上面的例子中，访问方式不优雅，Python提供了内置的函数

# 内建函数：
# getattr(object, name[,default]):通过name返回object的属性值，当属性不存在，将使用default返回，如果没有default，则抛出AttributeErroe。name必须为字符串
# setattr(object, name, vaule): object的属性存在，则覆盖，不存在，则新增
# hasattr(object, name):判断对象是否有这个名字的属性，name必须为字符串


p1 = Point(10, 10)
print(repr(p), repr(p1), sep='\n')
print(p.__dict__)
setattr(p1, 'y', 16)
setattr(p1, 'z', 12)
print(getattr(p1, '__dict__'))


# 动态调用方法
if hasattr(p, 'show'):
    getattr(p, 'show')()

# 动态增加方法，为类增加方法
if not hasattr(Point, 'add'):
    setattr(Point, 'add', lambda self, other: Point(self.x+other.x, self.y+other.y))

print(Point.add)     # 程序在内存中执行时候才知道Point有此add属性
print(p.add)
print(p.add(p1))  # 绑定

# 为实例增加方法，未绑定
if not hasattr(p, 'sub'):
    setattr(p, 'sub', lambda self, other: Point(self.x-other.x, self.y-other.y))

print(p.sub(p, p))

print(p.sub)

print(Point.__dict__)
print(p.__dict__)

# 思考：这种动态增加属性的方式和装饰器修饰一个类、Mixin方式的差异？
# 这种动态增删属性的方式是运行时改变类或者实例的方式，
# 但是装饰器或Mixin都是定义时就决定了，因此反射能力具有更大的灵活性。

