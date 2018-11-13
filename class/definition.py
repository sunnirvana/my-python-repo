# Doc Desc
# 类定义样例: 类属性, 实力属性, 类方法, 实例方法, 动态添加属性与方法
# 特殊方法 (special methods)
# __str__, __slot__, __repr__,

import types


class Person(object):
    """一个简单的类实例"""
    count = 0  # public 类属性, 共享于实例之间
    __count = 0  # private 类属性

    # 用tuple定义允许绑定的属性名称
    # !! 在类中定义的属性和方法也受到__slots__限制，所以需要添加所有的[实例属性]和[实例方法]
    __slots__ = ('name', 'age', '_gender', '__job', 'say_hi')

    @classmethod  # 类方法
    def show_count(cls):
        return Person.__count

    # 构造函数
    def __init__(self, name='Bob', gender='male', job='IT'):
        self.name = name  # public 实例属性
        self._gender = gender  # protected 实例属性
        self.__job = job  # private 实例属性
        # self.__name__ = 'my class'  # 一般用作特殊属性
        Person.count = Person.count + 1  # 访问类属性
        Person.__count = Person.count

    def show_props(self):
        return ' '.join(['Hello', self.name, '(', self._gender, self.__job, ')'])


def fn_say_hi(self, name):
    # print(self, name)
    print("Hi, ", name)


def main():
    # 实例化
    p1 = Person()
    print("Class count: ", Person.count)
    print("Class internal count: ", Person.show_count())

    p2 = Person('Zhang san')
    print("Class count: ", Person.count)
    print("Class internal count: ", Person.count)

    # 访问类的属性，方法
    print("Instance p1 name:", p1.name)
    print("Instance p1 gender:", p1._gender)
    # Error happens: AttributeError: 'Person' object has no attribute '__job'
    try:
        print("Instance p1 job:", p1.__job)
    except AttributeError:
        print("Attribute Error")

    print("Instance ", p1.__class__, ": ", p1.show_props())
    print("Instance p2 name:", p2.name)
    print("Instance p2 gender:", p2._gender)
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

    # 动态添加实例方法
    print("Bind instance method say_hi: ")
    p1.say_hi = types.MethodType(fn_say_hi, p1)
    p1.say_hi("I'm from external")
    try:
        p2.say_hi("Am I here?")
    except AttributeError:
        print("p2 has no say_hi method")
    # 删除实例方法
    print("Delete instance method say_hi")
    del p1.say_hi
    try:
        p1.say_hi("Am I here?")
    except AttributeError:
        print("p1 has no say_hi method")


if __name__ == '__main__':
    main()
