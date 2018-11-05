#!!! Python2 !!! -- reduce
# Python的 decorator 本质上就是一个高阶函数，它接收一个函数作为参数，然后，返回一个新函数。
# 使用 decorator 用Python提供的 @ 语法，这样可以避免手动编写 f = decorate(f) 这样的代码。

# 计算函数调用的时间可以记录调用前后的当前时间戳，然后计算两个时间戳的差。

# decorator without args
import time
from functools import reduce


def performance(f):
    def fn(*args, **kw):
        start = time.time()
        r = f(*args, **kw)
        end = time.time()
        print('call %s() in %fs' % (f.__name__, (end-start)))
        return r
    return fn


@performance
def factorial(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


print(factorial(10))

# decorator with args -- 3层嵌套的decorator


def performance2(unit):  # 第1层, 对外
    def perf_decorator(f):  # 第2层, 接收unit参数并处理
        def wrapper(*args, **kw):  # 第3层, 调用外部函数
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator


@performance2('ms')
def factorial2(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


print(factorial(10))

# decorator with functools -- 复制原函数的一些属性到新函数中, 无法获得原函数的原始参数信息
import functools


def performance3(unit):
    def perf_decorator(f):
        @functools.wraps(f)  # 修改封装函数
        def wrapper(*args, **kw):
            t1 = time.time()
            r = f(*args, **kw)
            t2 = time.time()
            t = (t2 - t1) * 1000 if unit == 'ms' else (t2 - t1)
            print('call %s() in %f %s' % (f.__name__, t, unit))
            return r
        return wrapper
    return perf_decorator


@performance3('ms')
def factorial3(n):
    return reduce(lambda x, y: x*y, range(1, n+1))


# print factorial(10)
print(factorial.__name__)
