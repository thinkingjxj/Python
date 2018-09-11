import sqlalchemy
import pymysql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker


host = '192.168.86.100'
port = '3306'
user = 'root'
password = '123456'
database = 'test'

conn_str = 'mysql+pymysql://<{}>:<{}>@<{}>:<{}>/<{}>'.format(user, password, host, port, database)
engine = sqlalchemy.create_engine(conn_str, echo=True)

# 创建基类，便于实体类继承
Base = declarative_base()

# 创建实体类

class Student(Base):
    # 指定表名
    __tablename__ = 'student'
    # 定义属性对应字段
    id = Column(Integer, primary_key=True)
    name = Column(String(64), nullable=False)
    age = Column(Integer)

    def __repr__(self):
        return "{}: id={}, name={}, age={}".format(self.__class__.__name__, self.id, self.name, self.age)

s = Student(name='tom')
print(s.name)
s.age = 20
print(s.age)

