class Employee:
    def __init__(self, name, salary=0):  # 初始化
        self.name = name
        self.salary = salary

    def giveRaise(self, percent):  # 加薪
        self.salary = self.salary + (self.salary * percent)

    def work(self):  # 工作
        print(self.name, 'does stuff')

    def __repr__(self):  # 打印
        return '<Employee: name=%s, salary=%s>' % (self.name, self.salary)


class Chef(Employee):  # 厨师
    def __init__(self, name):
        Employee.__init__(self, name, 50000)

    def work(self):
        print(self.name, 'makes food')


class Server(Employee):  # 服务员
    def __init__(self, name):
        Employee.__init__(self, name, 40000)

    def work(self):
        print(self.name, 'interfaces with customers')


class PizzaRobot(Chef):  # 机器人厨师
    def __init__(self, name):
        Chef.__init__(self, name)

    def work(self):
        print(self.name, 'makes pizza')


if __name__ == '__main__':
    bob = PizzaRobot('Bob')
    print(bob)      # Employee: name=Bob, salary=50000
    bob.work()      # Bob makes pizza
    bob.giveRaise(0.20)
    print(bob)       # Employee: name=Bob, salary=60000
    print()

    # 下面的for循环创建了4个类的实例
    for klass in Employee, Chef, Server, PizzaRobot:
        obj = klass(klass.__name__)
        obj.work()      # Empolyee does stuff
                        # Chef makes food
                        # Server interfaces with customers
                        # Pizzarobot makes pizza

