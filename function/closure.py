

def createCounter1():
    # 一、在内部函数内修改外部函数局部变量的两种方法
    # 1法：把外部变量变成容器或者说可变变量
    a = [0]

    def counter():
        a[0] += 1
        return a[0]
    return counter


def createCounter2():
    # 2法：在内部函数里给予外部函数局部变量nonlocal声明，让内部函数去其他领域获取这个变量
    a = 0

    def counter():
        nonlocal a
        a += 1
        return a
    return counter


def createCounter3():
    # 二、在内部函数内修改全局变量
    global a
    a = 0

    def counter():
        global a
        a += 1
        return a
    return counter


# 测试:
for createCounter in [createCounter1, createCounter2, createCounter3]:
    counterA = createCounter()
    print(counterA(), counterA(), counterA(),
          counterA(), counterA())  # 1 2 3 4 5
    counterB = createCounter()
    if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
        print('测试通过!')
    else:
        print('测试失败!')
