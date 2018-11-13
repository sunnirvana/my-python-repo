"""[summary]
    测试特殊方法
        __str__(self) 显示类信息给用户
        __repr__(self) 显示类信息给开发人员
        __len__(self) 返回长度，可用于len(Fib())
        __iter__(self) 用于迭代 (for x in Fib()...)
        __getitem__(self, n) 类似list索引操作l[5]

Returns:
    [type] -- [description]
"""


class Fib(object):
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num):
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    __repr__ = __str__

    def __len__(self):
        return len(self.numbers)


class FibIter():
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
            # 实力本身就是迭代对象，所以返回 self
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 10:
            # TODO: 两者区别
            # raise StopIteration()
            # raise StopIteration
            raise StopIteration()
        return self.a

    def __getitem__(self, n):
        # 如果想要更丰富的支持slice操作，比如负数，步长等等，是个挺复杂的操作
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        elif isinstance(n, slice):
            if n.start is None:
                start = 0
            else:
                start = n.start

            if n.stop is None:
                stop = 11  # 11 by default
            else:
                stop = n.stop

            a, b, L = 1, 1, list()
            for x in range(stop):
                a, b = b, a+b
                if x >= start:
                    L.append(a)
            # print(L)
            return L


print("simple Fib")
f = Fib(10)
print(f)
print(len(f))

print("Iterable Fib __iter__() __next__()")
f2 = FibIter()
for n in f2:
    print(n)

print("Index accessable Fib __getitem__()")
print(f2[5])


print("Slice Fib __getitem__()")
print(f2[1:5])
print(f2[:5])
print(f2[1:])
# FibIter()[::2]
