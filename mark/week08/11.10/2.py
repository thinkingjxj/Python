
class PrintableMixin:
    def print(self):
        print(self.content, 'Mixin')

class Document:
    def __init__(self, content):
        self.content = content

class Pdf(Document): pass
class Word(Document): pass

class SuperPrintableMixin(PrintableMixin):
    def print(self):
        print('~'*20)
        super().print()  # 通过继承复用
        print('~'*20)

class SuperPrintablePdf(SuperPrintableMixin, Pdf): pass

print(SuperPrintablePdf.__dict__)
print(SuperPrintablePdf.mro())


spp = SuperPrintablePdf('super print pdf')
spp.print()

# Mixin本质上就是多继承实现的
# Mixin体现的是一种组合的设计模式
# 在面向对象的设计中，一个复杂的类，往往需要很多功能，而这些功能有来自不同的类提供
# 这就需要很多的类组合在一起
# 从设计模式的角度来说，多组合、少继承
# Mixin类的使用原则：
# Mixin类中不应该显式的出现__init__初始化方法
# Mixin类通常不能独立的工作，因为它是准备汇入别的类中的部分功能实现
# Mixin类的祖先也应该是Mixin类
