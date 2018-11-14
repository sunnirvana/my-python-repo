# -*- coding: utf-8 -*-

'''
关键字
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 
'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 
'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
'''
import keyword
# print(keyword.kwlist)

'''
基本数据类型 
不可变: Number, String, Tuple, 
可变: List, Set, Dictionary

Number: int, bool, float, complex (复数)

String:
单引号和双引号作用完全相同

'''
# Number
a, b, c, d, e = 20, 4.4, 3E-2, True, 4+3j
print(a, b, c, d, e, type(a), type(b), type(c),
      type(d), type(e), isinstance(a, complex))

print(3+2, 4.3-2, 3*7, 3/4, 2//4, 17 % 3, 2**5)

# String
str = "Runoob"
print(str, str[0:-1], str[0], str[2:5], str[-3:-1],
      str[3:-2], str * 2, 'Hello ' + str)  # str[m:n] 取值范围是[m,n)，左闭右开的字符串区间

# List
list = ['a', 32, 2.21, 'hello', 1]
print(list, list[0], list[-3:-1], list+['ha', 'no'], list*2)
list[0] = 'b'
list[1] = 12
print(list, list[0], list[-3:-1], list+['ha', 'no'], list*2)

# Tuple
tuple = ('a', 32, 2.21, 'hello', 1)
tuple_empty = ()
tuple_one = ('b')  # 这个不是元组，只能相当于一个字符串变量
tuple_one2 = ('b',)
print(tuple, tuple[0], tuple[-3:-1], tuple*2,
      tuple_empty, tuple_empty, tuple_one, tuple_one2, type(tuple_one), type(tuple_one2))

# Set 是一个无序不重复元素的序列
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
print(student)
set_a = set('abasdgasdfra')  # f,d,a,g,s,r,b
set_b = set('asngasdfg')  # f,d,a,g,s,n
print(set_a, set_b)
print(set_a-set_b, set_b-set_a, set_a | set_b, set_a &
      set_b, set_a ^ set_b)  # ^ 不同时存在于set_a和set_b的元素

# Dictionary
dict = {}
dict['one'] = '11111'
dict[2] = '22222'
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(dict['one'], dict, tinydict, tinydict.keys,
      tinydict.items, tinydict.values)

# print(dict([('Runoob', 1), ('Google', 2), ('Alibaba', 3)]))
print({x: x**2 for x in (2, 4, 6)})
# print(dict(Runoob=1, Google=2, Alibaba=3))

print('abc', repr('abc'))

'''
算术运算符:
+, -, *, / (得到小数), // (得到整数), %/ (取余), ** (乘方)
Python会把整型转换成为浮点数

比较运算符
==, !=, >, <, >=, <=

赋值运算符
=, +=, -=, *=, /=, %=, **=, //=

位运算符
&, |, ^, ~, >>, <<

逻辑运算符
and, or, not

成员运算符
in, not in

身份运算符
is, not is
判断两个标识符是不是引用同一个对象

'''

a = 10
b = 20
list = [1, 2, 3, 4, 5]

if (a in list):
    print('存在')
else:
    print('不存在')

if (a not in list):
    print('不存在')
else:
    print('存在')

'''
is 与 == 区别：
is 用于判断两个变量引用对象是否为同一个， == 用于判断引用变量的值是否相等。
'''
a = [1, 2, 3]
b = a
print(b is a, b == a, a, b, id(a), id(b))
b = a[:]
print(b is a, b == a, a, b, id(a), id(b))
