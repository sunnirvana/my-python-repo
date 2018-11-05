# 高阶函数. 返回值为函数
from functools import reduce


def calc_prod(lst):
    def lazy_prod():
        def prod(x, y):
            return x * y
        return reduce(prod, lst)
    return lazy_prod


f = calc_prod([1, 2, 3, 4])
print(f())
