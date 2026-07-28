"""
1. 创建线程的流程是什么？
    a. 导入线程模块
        import threading
    b. 创建子线程并指定执行的任务
        sub_thread = threading.Thread(target=任务名)
    c. 启动线程执行任务
        sub_thread.start()

2. 线程传参的两种方式是什么？
    a.元组方式传参：元组方式传参一定要和参数的顺序保持一致。
    b.字典方式传参：字典方式传参字典中的key一定要和参数名保持一致
"""

"""
案例: 线程入门案例, 一边听音乐, 一边写代码.

线程的使用步骤:
    1. 导包
    2. 创建线程对象.
    3. 启动线程.

线程和进程的关系:
    1. 进程是CPU分配资源的基本单位, 线程是CPU调度资源的最小单位.
    2. 线程是依附于进程的, 每个进程至少有1个线程(主线程栈)
    3. 进程间数据相互隔离, (同一个进程的)线程间数据可以共享.
"""

# 导包
import threading
import time


# 1. 定义函数，表示：敲代码。
def coding():
    for i in range(1, 11):
        time.sleep(0.1)
        print(f'正在敲第 {i} 遍代码...')


# 2. 定义函数，表示：听音乐。
def music():
    for i in range(1, 11):
        time.sleep(0.1)
        print(f'正在听第 {i} 首音乐...')


# 3. 测试
if __name__ == '__main__':
    # 4. 创建两个线程对象，分别关联上述的两个目标函数。
    t1 = threading.Thread(target=coding)
    t2 = threading.Thread(target=music)

    # 写在线程启动前时，线程是不启动的。无法跟主进程抢资源，因此下述代码会最先执行。
    for i in range(5):
        time.sleep(0.1)
        print('我是main')

    # 5. 启动线程
    t1.start()
    t2.start()

    # 写在线程启动之后，则线程和主进程可以抢资源，因此下面的代码和t1，t2的代码抢资源随机执行
    for i in range(5):
        time.sleep(0.1)
        print('我是main～～～')
