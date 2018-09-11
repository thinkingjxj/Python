d = {
    'a': 20
}


class DictObj:
    def __init__(self, d: dict):
        if isinstance(d, (dict,)):
            self.__dict__['_dict'] = d
        else:
            self.__dict__['_dict'] = {}
        # self._dict = d  # 此句会调用__setattr__()这个方法，写pass的话，，产生递归错误

    def __getattr__(self, item):  # 处理不好会产生递归，为什么？产生递归了可以用内部的__dict__改造
        try:
            return self._dict[item]
        except KeyError:
            raise AttributeError('Attribute {} not found.'.format(item))

    def __setattr__(self, key, value):
        # 不允许设置属性
        raise NotImplementedError
        # pass

do = DictObj(d)
print(do.a)
do.a = 15
print(do.a)
