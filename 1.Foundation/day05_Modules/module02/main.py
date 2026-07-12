# 导入自定义模块
import my_func

# 使用模块中的功能
print(my_func.PI)
print(my_func.NAME)

# 导入自定义模块中的功能
from my_func import log_separator1, log_separator3

log_separator1()
log_separator3()

# __all__ 指定 from ... import * 导入的是哪些功能
from my_func import *

print(PI)
# log_separator2()    # 报错


"""
小结：

__name__ 和 __all__ 作用详解
一、__name__
它是 Python 内置特殊变量，用于标识当前模块的名称：
模块直接被运行：__name__ 的值固定为 __main__，常用写法if __name__ == "__main__":，可以把仅模块自身运行时才执行的测试代码放在这个判断里，被导入时不会执行这部分内容。
模块被其他文件导入：__name__ 的值等于该模块的文件名（不带.py后缀）。

二、__all__
专门约束 from 模块名 import * 这种批量导入行为：
它是一个字符串列表，列表里填写的变量、函数、类名称，才会在使用import *时被导入；
没写进列表的内容，不会被*批量导入，能避免命名污染、控制模块对外暴露的接口；
该规则只对import *生效，显式指定导入from 模块 import 某个内容或者import 模块的方式不受它限制。
"""
