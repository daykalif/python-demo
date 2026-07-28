"""
进程编号的作用:
- 进程编号唯一标识一个进程，方便管理进程。
        在一个操作系统中，一个进程拥有的进程号是唯一的，进程号可以反复使用。
- 获取进程编号的目的是验证主进程和子进程的关系，可以得知子进程是由那个主进程创建出来的

获取进程编号的两种操作:
- 获取当前进程编号
- 获取当前父进程编号
"""
# 导包
import multiprocessing
import time
import os


# 需求：小明一边敲代码，一边听音乐。
# 1. 定义函数，表示敲代码。
def coding(name, num):
    for i in range(1, num + 1):
        time.sleep(0.1)  # 模拟耗时操作，更好的查看多任务的执行结果
        print(f'{name} 正在敲第 {i} 行代码...')
    print(f"p1两种获取进程的方式，pid是：{os.getpid()}/{multiprocessing.current_process().pid}")
    print(f"p1父进程，ppid是：{os.getppid()}")


# 2. 定义函数，表示听音乐。
def music(name, count):
    for i in range(1, count + 1):
        time.sleep(0.1)  # 模拟耗时操作，更好的查看多任务的执行结果
        print(f'{name} 正在听第 {i} 首歌...........')
    print(f"p2两种获取进程的方式，pid是：{os.getpid()}/{multiprocessing.current_process().pid}")
    print(f"p2父进程，ppid是：{os.getppid()}")


# 3.创建主进程(主线程)
if __name__ == '__main__':
    # 4. 创建两个子进程，分别关联上述的目标函数。
    p1 = multiprocessing.Process(target=coding, args=('虚竹', 10))
    p2 = multiprocessing.Process(target=music, kwargs={'count': 20, 'name': '刘备'})

    # 5. 开启子进程。
    p1.start()
    p2.start()

    # 6.查看主进程的pid
    print(f"主进程的pid是：{os.getpid()}/{multiprocessing.current_process().pid}")
    # 7.查看主进程的父进程ppid
    print(f"主进程的ppid是：{os.getppid()}")
