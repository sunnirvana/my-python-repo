class MyClass:
    """一个简单的类实例"""
    i = 123

    def func(self):
        return 'Hello world'


def run():
    # 实例化
    x = MyClass()

    # 访问类的属性，方法
    print("MyClass 类的属性 i 为", x.i)
    print("MyClass 类的方法 func 输出为: ", x.func())
