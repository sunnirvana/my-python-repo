# -*- encoding:utf-8 -*-

# 包是一种管理 Python 模块命名空间的形式，采用"点模块名称"。
# 比如一个模块的名称是 A.B， 那么他表示一个包 A中的子模块 B 。

from . sub_package_a import module_a
from . sub_package_b import module_b

__version__ = "0.1.0"
# 导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，
# 那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入
__all__ = ['module_a', 'module_b']
