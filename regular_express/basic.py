# -*- coding: utf-8 -*-
'''
1. 特殊字符
1) ^ $ * ? + {2} {2,} {2,5} |
2) [] [^] [a-z] .
3) \s \S \w \W
4) [\u4E00-\u9FA5] () \d
'''
__author__ = 'Yubo'

import re


def run(line, regrex_str):
    print("\n" + line)
    for str in regrex_str:
        match_obj = re.match(str, line)
        if (match_obj):
            for group in match_obj.groups():
                print(str + ':\t\t' + group)
        else:
            print(str + ':\t\t' + 'not match')


line = "bobby123"
regrex_str = "^b.*"
if re.match(regrex_str, line):
    print('yes')
else:
    print('no')

# . * {}
# 默认是贪婪模式；在量词后面直接加上一个问号？就是非贪婪模式。
# 使用?取消贪婪模式，获取尽可能长的匹配结果
line = "booooooooobbbbby123"
regrex_str = (
    ".*(b.*b).*",  # 贪婪
    ".*?(b.*b).*",  # 非贪婪
    ".*?(b.*?b).*",  # 非贪婪
    ".*(b.+b).*",
    ".*?(b.+b).*",
    ".+?(b.+b).*",
    ".*?(b.+?b).*"
)
run(line, regrex_str)

# | (or)
line = 'boddy123'
regrex_str = (
    '(boddy|boddy123)',
    '(boddy123|boddy)',
    '(boddy|booddy)123',
    '((boddy|booddy)123)'
)
run(line, regrex_str)

# [] {}
line = '1341452423'
regrex_str = (
    '(1[34578][0-9]{8})',
    '(1[34578][^1][0-9]{7})'
)
run(line, regrex_str)

# \s (一个空格) \S (一个不是空格) \w ([A-Za-z0-9_]) \W
line = '你  好'
regrex_str = (
    r'(你\s好)',
    r'(你\s+好)',
    r'(你\W好)',
    r'(你\W+好)',
)
run(line, regrex_str)

line = '你bb好'
regrex_str = (
    r'(你\S好)',
    r'(你\S+好)',
)
run(line, regrex_str)

line = '你b好'
regrex_str = (
    r'(你\w好)',
    r'(你[A-Za-z0-9_]好)',
)
run(line, regrex_str)

# [\u4E00-\u9FA5] 汉字
line = 'study in 南京大学'
regrex_str = (
    r'.*([\u4E00-\u9FA5]+)',
    r'.*?([\u4E00-\u9FA5]+)',
    r'.*?([\u4E00-\u9FA5]+大学)',
    r'.*([\u4E00-\u9FA5]+)[\u4E00-\u9FA5]{2}$',
    r'.*?([\u4E00-\u9FA5]+)[\u4E00-\u9FA5]{2}$',
)
run(line, regrex_str)

# \d
line = '出生于2014年3月31日'
regrex_str = (
    r'.*(\d+)年.*',  # 贪婪
    r'.*?(\d+)年.*',  # 非贪婪
    r'出生于(\d{,4})[\u4E00-\u9FA5|-](\d{,2})[\u4E00-\u9FA5|-](\d{,2})[\u4E00-\u9FA5|-]',
)
run(line, regrex_str)
