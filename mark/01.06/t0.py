import pymysql


class Field:
    def __init__(self, name, column=None, pk=False, unique=False, index=False, nullable=True, default=None):
        self.name = name
        if column is None:
            self.column = name
        else:
            self.column = column
        self.pk = pk
        self.unique = unique
        self.index = index
        self.nullable = nullable
        self.default = default

    def validate(self, value):
        raise NotImplementedError  # 基类不实现

    def __get__(self, instance, owner):
        # 返回值应该是owner的实例instance的属性
        if instance is None:
            return self
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self.name] = value

    def __str__(self):
        return "{} <{}>".format(self.__class__.__name__, self.name)

    __repr__ = __str__


# 实现int字段类和string字段类
class IntField(Field):
    def __init__(self, name, column=None, pk=False, unique=False, index=False,
                 nullable=True, default=None, auto_increament=False):
        super().__init__(name, column, pk, unique, index, nullable, default)
        self.auto_increament = auto_increament

    def validate(self, value):
        # 思考什么不可以为空
        if value is None:
            if self.pk:
                raise TypeError()
            if not self.nullable:
                raise TypeError()
        else:
            if not isinstance(value, int):
                raise TypeError()


class StringField(Field):
    # 需要增加一个长度属性
    def __init__(self, name, column=None, pk=False, unique=False, index=False,
                 nullable=False, default=False, length=False):
        super().__init__(name, column, pk, unique, index, nullable, default)
        self.length = length

    def validate(self, value):
        if value is None:
            if self.pk:
                raise TypeError()
            if not self.nullable:
                raise TypeError()
        else:
            if not isinstance(value, str):
                raise TypeError()
            if len(value) > self.length:
                raise ValueError()


# student类的实现
class Student:
    id = IntField('id', 'id', True, nullable=False, auto_increament=True)
    name = StringField('name', nullable=False, length=64)
    age = IntField('age')

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age

    def __str__(self):
        return "Student({}, {}, {})".format(self.id, self.name, self.age)

    __repr__ = __str__

    def save(self, session:Session):
        sql = "insert into student (id, name, age) values (%s, %s, %s)"
        session.excute(sql, (self.id, self.name, self.age))



class Session:
    def __init__(self, conn:pymysql.connections.Connection):
        self.conn = conn
        self.cursor = None

    def excute(self, query, *args):
        if self.cursor is None:
            self.cursor = self.conn.cursor()
        self.cursor.excute(query, args)

    def __enter__(self):
        self.cursor = self.conn.cursor
        return self  # 以后调用的是session对象的excute

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        if exc_type:
            self.conn.roolback()
        else:
            self.conn.commit()



