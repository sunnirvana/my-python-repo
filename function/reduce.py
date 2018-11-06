' Use reduce '
from functools import reduce


DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def char2num(s):
    return DIGITS[s]


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


def str2float(s):
    [x, y] = s.split('.')
    # print(x, y)
    x = str2int(x)
    l = len(y)
    y = str2int(y)
    return x + (y / pow(10, l))


# print(str2int('123'))
# print(str2float('0.123'))
for s in ['0.123', '10.123', '10.0']:
    num = str2float(s)
    if isinstance(num, float):
        print('Float: %f' % num)
    else:
        print('Not a float')
print('str2float(\'123.456\') =', str2float('123.456'))
if abs(str2float('123.456') - 123.456) < 0.00001:
    print('测试成功!')
else:
    print('测试失败!')
