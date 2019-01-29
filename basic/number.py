# -*- coding: utf-8 -*-
a = [10.123, 10.124, 10.125, 10.126, 11.123, 11.124, 11.125, 11.126]
b = [10.113, 10.114, 10.115, 10.116, 11.113, 11.114, 11.115, 11.116]

for num in a:
    print(num, ' => ', round(num, 2))

print('=================')

for num in b:
    print(num, ' => ', round(num, 2))

a, b = 0, 1
while a < 100000:
    print(a, end=',')
    a, b = b, a+b

a = 10


def test(a):
    a = a+1
    print(a)


test(a)

list = [1, 2, 3, 4, 5]
print(list)
list.remove(2)
print(list)
try:
    list.remove(10)
except Exception as e:
    print('error', e)
print(list)
