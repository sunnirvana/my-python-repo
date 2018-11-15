
"""[summary]
    特殊方法测试
        __getattr__(self, attr) 当调用不存在的属性时，解释器会试图调用__getattr__(self, 'score')来尝试获得属性
        __call__(self)，实现后可以直接对实例进行调用 
"""


class Student():
    def __init__(self):
        pass

    def __getattr__(self, attr):
        if attr == 'name':
            return 'yubo'

        if attr == 'age':
            return lambda: 25

        # raise Error for no such attribute, otherwise it returns 'None' by default,
        raise AttributeError("'Student' object has no attribute '%s'" % attr)

    def __call__(self):
        print('I\'m  Student class')


class Chain():
    def __init__(self, path):
        self._path = path

    def __getattr__(self, path):
        return Chain('%s/%s' % (self._path, path))

    def __str__(self):
        return self._path

    __repr__ = __str__


if __name__ == '__main__':
    s1 = Student()
    # s1.name = 'yubo'
    print('>>> Dynamically define props')
    print(s1.name)
    print(s1.age())
    try:
        print(s1.aaa)
    except AttributeError as e:
        print(e)

    print('>>> call Student class')
    # 通过callable()函数，我们就可以判断一个对象是否是“可调用”对象
    if callable(s1):
        print('it is callable')
        s1()
    else:
        print('it is not callable')

    print('>>> use __getattr__ to implement a chain class')
    c1 = Chain('/root').home.yubo.workspace.projects
    print(c1)
