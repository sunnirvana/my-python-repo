# 导入一个模块
import support
support.print_func("Bob")

import fibo
fibo.fib(10)
print(fibo.fib2(10))

# 内置的函数 dir() 可以找到模块内定义的所有名称。
print(dir(fibo))

# 导入一个模块的所有名字(变量和方法)，但不包括由单一下划线(_)开头的名字
from fibo import *
fib(10)
print(fib2(10))

# 按需求导入一个模块的某几个名字(变量和方法)
from fibo import fib, fib2
fib(10)
print(fib2(10))

# 每个模块都有一个__name__属性，当其值是'__main__'时，表明该模块自身在运行，否则是被引入
if __name__ == '__main__':
    print('程序本身在运行')
else:
    print('我来自另一个模块')

# 导入一个包及其子包
import package
package.sub_package_a.module_a.func_a()
package.sub_package_b.module_b.func_b()

# 导入一个具体的包
from package.sub_package_b.module_b import func_b
func_b()

# 导入一个包的所有的子模块
# 导入语句遵循如下规则：如果包定义文件 __init__.py 存在一个叫做 __all__ 的列表变量，
# 那么在使用 from package import * 的时候就把这个列表中的所有名字作为包内容导入
from package import *
print(package.__all__)
module_a.func_a()
module_b.func_b()
