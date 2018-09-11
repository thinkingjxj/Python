class PrintableMixin:
    def print(self):
        print(self.content, 'Mixin')

class Document:  # 第三方库，不允许修改
    def __init__(self, content):
        self.content = content


class Word(Document): pass  # 第三方库，不允许修改


class Pdf(Document): pass  # 第三方库，不允许修改


class PrintableWord(PrintableMixin, Word): pass


print(PrintableWord.__dict__)
print(PrintableWord.mro())

pw = PrintableWord('test string')
pw.print()

# Mixin就是其他类混合进来，同时带来了类的属性和方法
# 这里看来Mixin类和装饰器效果一样，也没有什么特别的，但是Mixin是类，就可以继承

















