import types


class Person(object):
    """一个简单的类实例"""
    count = 0  # public 类属性, 共享于实例之间
    __count = 0  # private 类属性

    @classmethod  # 类方法
    def show_count(cls):
        return Person.__count

    # 构造函数
    def __init__(self, name='Bob', sex='male', job='IT'):
        self.name = name  # public 实例属性
        self._sex = sex  # protected 实例属性
        self.__job = job  # private 实例属性
        # self.__name__ = 'my class'  # 一般用作特殊属性
        Person.count = Person.count + 1  # 访问类属性
        Person.__count = Person.count

    def show_props(self):
        return ' '.join(['Hello', self.name, '(', self._sex, self.__job, ')'])


def fn_say_hi(self, name):
    # print(self, name)
    print("Hi, ", name)
    pass


def main():
    # 实例化
    p1 = Person()
    print("Class count: ", Person.count)
    print("Class internal count: ", Person.show_count())
    # 给实例对象动态添加外部方法
    p1.say_hi = types.MethodType(fn_say_hi, p1)
    print("Class dynamical method: ")
    p1.say_hi("I'm from external")

    p2 = Person('Zhang san')
    print("Class count: ", Person.count)
    print("Class internal count: ", Person.count)

    # 访问类的属性，方法
    print("Instance p1 name:", p1.name)
    print("Instance p1 sex:", p1._sex)
    # Error happens: AttributeError: 'Person' object has no attribute '__job'
    try:
        print("Instance p1 job:", p1.__job)
    except AttributeError:
        print("Attribute Error")

    print("Instance ", p1.__class__, ": ", p1.show_props())
    print("Instance p2 name:", p2.name)
    print("Instance p2 sex:", p2._sex)
    print("Instance ", p2.__class__, ": ", p2.show_props())

    # Error happens: AttributeError: 'Person' object has no attribute '__job'
    try:
        print("Class p1 __count:", Person.__count)
    except AttributeError:
        print("Attribute Error")

    # 获取对象信息
    print(type(p1))  # 获取变量类型返回一个Type对象
    print(dir(p2))  # 获取变量的所有属性, 以列表形式, 包括具有特殊意义的属性
    print(getattr(p1, 'show_props'))  # 获取show_props属性
    print(getattr(p1, 'age', '20'))  # 获取age属性, 如果不存在就返回20
    setattr(p1, 'age', 20)  # 设置新属性
    print(getattr(p1, 'age'))  # 设置新属性


if __name__ == '__main__':
    main()
