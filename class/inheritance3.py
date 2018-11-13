# Doc Desc
# pprint, Pretty Print, 输出更美观 https://docs.python.org/3/library/pprint.html
# 本代码用于测试多重继承后, 对属性的操作, SubClass继承自BaseClass,TimesTwo, PlusFive
# 在SubClass的__init__中分别调用三个父类的__init__, 利用TimesTwo和PlusFive修改BaseClass中定义的属性

from pprint import pprint


class BaseClass():
    def __init__(self, value):
        self.value = value
        print('Init BaseClass')
        print('value is ', self.value)


class TimesTwo():
    def __init__(self):
        self.value *= 2
        print('Init TimesTwo')
        print('value is ', self.value)


class PlusFive(object):
    def __init__(self):
        self.value += 5
        print('Init PlusFive')
        print('value is ', self.value)


class SubClass(BaseClass, TimesTwo, PlusFive):
    def __init__(self, value):
        BaseClass.__init__(self, value)
        TimesTwo.__init__(self)
        PlusFive.__init__(self)


subClass = SubClass(1)
# print(SubClass.value)
pprint(SubClass.mro())
