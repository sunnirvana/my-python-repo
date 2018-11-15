# -*- coding: utf-8 -*-

'''
Python3中，已经使用Unicode作为内存中的字符存储方式，如下例子需要在Python2的环境演示
'''

import sys

# detect system default encoding
# 基本信息通过sys.platform就可以获得，引入platform可以获得更详细的系统信息
print(sys.platform, sys.getdefaultencoding())

s = "我爱Python"
su = u"我爱Python"

print('encode s: \t', s.decode('utf8').encode('utf8'))
# Python2 会报错，因为su目前还不是Unicode，所以不能被encode
print('encode su: \t', su.decode('utf8').encode('utf8'))
print('encode su: \t', su.encode('utf8'))
