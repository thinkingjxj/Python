import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, Date, Enum, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import or_, and_, not_
import enum

engine = sqlalchemy.create_engine("mysql+pymysql://root:123456@192.168.86.100:3306/test", echo=True)


# 创建基类
Base = declarative_base()


class MyEnum(enum.Enum):
    M = 'M'
    F = 'F'


class Employee(Base):
    __tablename__ = 'employees'
    emp_no = Column(Integer, primary_key=True)
    birth_date = Column(Date, nullable=False)
    first_name = Column(String(14), nullable=False)
    last_name = Column(String(16), nullable=False)
    gender = Column(Enum(MyEnum), nullable=False)
    hire_date = Column(Date, nullable=False)

    dept_emps = relationship('Dept_emp')

    def __repr__(self):
        return "{} no={} name={} gender={} no={}".format(self.__class__.__name__, self.emp_no,
                                                         self.first_name, self.last_name, self.gender.value,
                                                         self.dept_emps)


class Department(Base):
    __tablename__ = 'departments'
    dept_no = Column(String(4), primary_key=True)
    dept_name = Column(String(40), nullable=False, unique=True)

    def __repr__(self):
        return "{} no={} name={}".format(type(self).__name__, self.dept_no, self.dept_name)


class Dept_emp(Base):
    __tablename__ = 'dept_emp'

    emp_no = Column(Integer, ForeignKey('employees.emp_no', ondelete='CASCADE'), primary_key=True)
    dept_no = Column(String(4), ForeignKey('departments.dept_no', ondelete='CASCADE'), primary_key=True)
    from_date = Column(Date, nullable=False)
    to_date = Column(Date, nullable=False)

    def __repr__(self):
        return "{} empno={} deptno={}".format(type(self).__name__, self.emp_no, self.dept_no)


# 创建session
Session = sessionmaker(bind=engine)  # Produce a new class:
session = Session()  # invokes sessionmaker.__call__()


def show(emps):
    for x in emps:
        print(x)


emps = session.query(Employee).join(Dept_emp, Employee.emp_no == Dept_emp.emp_no).\
    filter(Employee.emp_no == 10010)
show(emps)
