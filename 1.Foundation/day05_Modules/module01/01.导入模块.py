# ----------------------- 1. 导入整个模块 import ... ---> 调用方式：模块名.功能名 / 别名.功能名 -----------------------

# 方式一：
import random

for i in range(100):
    print(random.randint(1, 100))

# 方式二：
import random as rd

for i in range(100):
    print(rd.randint(1, 100))

# ----------------------- 2. 导入模块中的功能 from ... import ... ---> 调用方式：功能名 / 别名 -----------------------
from random import randint

# 方式三：
for i in range(100):
    print(randint(1, 100))

# 方式四：
from random import randint as rint

for i in range(100):
    print(rint(1, 100))

# 方式五：
from random import *

for i in range(100):
    print(randint(1, 100))

# 方式六：
import random as rd

for i in range(100):
    print(rd.randint(1, 100))

"""
Python 模块知识点整理

1. 什么是模块？有什么用？
模块：就是一个 python 文件（.py后缀），文件里可以包含变量、函数、类，以及可直接执行的代码。
作用：提高代码复用性，降低开发门槛。

2. 导入模块的常用语法
导入模块的语句，一般写在 py 文件的开头，有三种常用写法：
import 模块名 [as 别名]
from 模块名 import 功能名 [as 别名]
from 模块名 import *

补充说明
第一种方式需要用模块名/别名.功能来调用模块内的内容；
第二种可以直接使用导入的功能名，也能给单独功能起别名；
第三种会一次性导入模块内所有内容，容易出现命名冲突，日常开发不推荐频繁使用。
"""
