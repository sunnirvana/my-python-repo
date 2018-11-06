import functools

int2 = functools.partial(int, base=2)
int8 = functools.partial(int, base=8)
kw = {'base': 16}
int16 = functools.partial(int, **kw)

print(int2('10'), int2('10100'), int2('101010001'))
print(int8('10'), int8('10100'), int8('101010001'))
print(int16('10'), int16('10100'), int16('101010001'))
