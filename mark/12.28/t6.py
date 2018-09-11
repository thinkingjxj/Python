import re
from wsgiref.simple_server import make_server
from webob import Response, Request, exc
from webob.dec import wsgify


class DictObj:
    def __init__(self, d: dict):
        if not isinstance(d, dict):
            self.__dict__['_dict'] = {}
        else:
            self.__dict__['_dict'] = d

    def __getattr__(self, item):
        try:
            return self._dict[item]
        except KeyError:
            raise AttributeError('Attribute {} Not Found'.format(item))

    def __setattr__(self, key, value):
        raise NotImplementedError


class Router:
    TypePatterns = {
        'str': r'[^/]+',
        'word': r'\w+',
        'int': r'[+-]?\d+',
        'float': r'[+-]?\d+\.\d+',
        'any': r'.+'
    }

    TypeCast = {
        'str': str,
        'word': str,
        'int': int,
        'float': float,
        'any': str
    }

    KVPATERN = re.compile('/({[^{}:]+:?[^{}:]*})')

    def transform(self, kv: str):

        name, _, type = kv.strip()
        return '/(?P<{}>{})'.format(name, self.TypePatterns.get(type, '\w+')), name, self.TypeCast.get(type, str)

    def parse(self, src: str):

        start = 0
        res = ''
        translator = {}  # id=>int  name=>str
        while True:
            matcher = self.pattern.search(src, start)
            if matcher:
                res += matcher.string[start:matcher.start()]
                tmp = self.transform(matcher.string[matcher.start():matcher.end()])
                res += tmp[0]
                translator[tmp[1]] = tmp[2]
                start = matcher.end()
            else:
                break
        # 没有任何匹配应该原样返回字符串
        if res:
            return res, translator
        else:
            return src, translator


    def __init__(self, rule, *methods):
        def wrapper(handler):
            pattern, translator = self._parse(rule)
            self.__routeable.append()





s = '/student/{name:str}/xxx/{id:int}'
s1 = '/student/xxx/{id:int}'
s2 = '/student/xxx/1234'
s3 = '/student/{name:}/xxx/{id}'
s4 = '/student/{name:}/xxx/{id:aaa}'


# 编写转换函数






print(parse(s))
print(parse(s1))
print(parse(s2))
print(parse(s3))
print(parse(s4))
