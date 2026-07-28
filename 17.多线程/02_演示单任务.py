"""
进程的概念
  专业定义：进程（Process）是CPU资源分配的最小单位，它是操作系统进行资源分配和调度运行的基本单位

  通俗理解：一个正在运行的程序就是一个进程
    举例：正在运行的QQ、微信等应用，各自都属于一个独立进程
"""

"""
进程是什么？
- 进程（Process）是操作系统 CPU 资源分配的最小单位

多进程的作用是什么？
- 多进程是 Python 程序中实现多任务的一种方式，使用多进程可以大大提高程序的执行效率．

Python 中多进程的基本工作方式？
- 程序运行起来形成主进程；在主进程上创建子进程
"""

"""
案例: 演示单任务, 前边不执行完毕, 后边绝对无法执行.
"""


# 1.定义函数A, 输出10次 hello world
def func_a():
    for i in range(10000000):
        print("hello world")


# 2. 定义函数B, 输出10次 hello python
def func_b():
    for i in range(10):
        print("hello python")


func_a()
print('-' * 23)
func_b()
