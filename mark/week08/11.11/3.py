# class Printable:
#     def _print(self):
#         print(self.content)
#
#
# class Document:
#     def __init__(self, content):
#         self.content = content
#
#
# class Word(Document): pass
#
#
# class Pdf(Document): pass
#
#
# class Printableword(Printable, Word): pass
#
#
# print(Printableword.__dict__)
# print(Printableword.mro())
# pw = Printableword('test string')
# pw._print()


class PrintableMixin:
    def print(self):
        print(self.content, 'Mixin')


# 装饰器：用装饰器增强一个类，把功能给类附加上去，哪个类需要，就装饰哪个

def printable(cls):  # 进去什么出来什么
    def _print(self):
        print(self.content,'装饰器')
    cls.print = _print
    return cls


class Document:  # 第三方库不允许修改
    def __init__(self,content):
        self.content = content

class Word(Document): pass  # 第三方库，不允许修改

class Pdf(Document): pass   # 第三方库，不允许修改

@printable
class Printableword(Word): pass

print(Printableword.__dict__)
print(Printableword.mro())
pw = Printableword('test string')
pw.print()

@printable
class PrintablePdf(Word): pass

class PrintableWord(PrintableMixin, Word):pass

p = Printableword('test string1')
p.print()
print(PrintableWord.__dict__)
print(PrintableWord.mro())
