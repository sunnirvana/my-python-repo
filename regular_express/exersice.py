# -*- coding: utf-8 -*-
'''
正则表达式的练习
'''
import re

contents = (
    'XXXX出生于2001年6月1日',
    'XXXX出生于2001-6-1',
    'XXXX出生于2001/6/1',
    'XXXX出生于2001-06-01',
    'XXXX出生于2001-6',
    'XXXX出生于2001-06',
)

# regrex_str = r'^([\u4E00-\u9FA5]+)出生于(\d{,4})[\u4E00-\u9FA5|-|/](\d{,2})[\u4E00-\u9FA5|-|/]?(\d{,2})[\u4E00-\u9FA5]?'
regrex_str = r'^([\w\u4E00-\u9FA5]+)出生于(\d{0,4})[\u4E00-\u9FA5/-](\d{0,2})[\u4E00-\u9FA5/-]?(\d{0,2})?[\u4E00-\u9FA5/-]?'
# regrex_str = r'^([\w|\u4E00-\u9FA5]+)出生于(\d{0,4}).*'

print(regrex_str)
for content in contents:
    match_obj = re.match(regrex_str, content)
    print(content + ' \t', end='')
    if (match_obj):
        groups = match_obj.groups()
        for k, v in enumerate(groups):
            print(k, v, end=', ')
            pass
        print('')
    else:
        print('not match')
    pass
