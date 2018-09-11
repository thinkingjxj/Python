# 实现华氏温度和摄氏温度的转换
# C = 5x(F-32)/9
# F = 9xC/5+32
# 增加与开氏温度的转换：K = C + 273.15

class Temperature:
    def __init__(self, t, unit='c'):
        '''
        温度类：提供温度的转换
        :param t: 温度
        :param unit: 单位，k为开氏，c为摄氏，f为华氏
        '''
        self._c = None
        self._f = None
        self._k = None

        if unit == 'k':
            self._c = self.k2c(t)
            self._k = t
        elif unit == 'f':
            self._c = self.f2c(t)
            self._f = t
        else:
            self._c = t
    @property
    def k(self):
        if self._k is None:
            self._k = self.c2f(self._c)
        return self._k
    @property
    def c(self):
        return self._c
    @property
    def f(self):
        self._f = self.c2f(self._c)
        return self._f
    @classmethod
    def c2f(cls,c):
        return c + 273.15
    @classmethod
    def f2c(cls,f):
        return (f-32)*5/9
    @classmethod
    def c2k(cls,c):
        return c + 273.15
    @classmethod
    def k2c(cls,k):
        return k - 273.15
    @classmethod
    def f2k(cls,f):
        return cls.c2f(cls.f2c(f))
    @classmethod
    def k2f(cls,k):
        return cls.c2f(cls.k2c(k))
