class Temperate:
    def __init__(self, t, unit='c'):
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
    def c(self):
        return self._c
    @property
    def k(self):
        if self._k is None:
            self._k = self.c2f(self._c)
        return self._k
    @property
    def f(self):
        if self._f is None:
            self._f = self.c2f(self._c)
        return self._f

    @classmethod
    def k2c(cls, k):
        return k - 273.15
    @classmethod
    def c2k(cls, c):
        return c + 273.15
    @classmethod
    def f2c(cls, f):
        return (f-32)*5/9
    @classmethod
    def c2f(cls, c):
        return c*9/5+32
    @classmethod
    def f2k(cls, f):
        return cls.c2k(cls.f2c(f))
    @classmethod
    def k2f(cls,k):
        return cls.k2c(cls.c2f(k))


