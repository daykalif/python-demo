"""
案例：演示多线程共享全局变量，可能出现的问题。

多线程共享全局变量，出现问题的问题：
    累加次数不够。
产生原因：
    线程1还没有来得及执行完(一个完整的动作)前，被线程2抢走了资源，就可能出问题。
解决方案：
    加锁思想，即：互斥锁。
"""

# 需求：定义两个函数，分别对全局变量累加100W次，创建两个线程，关联这两个函数，执行看效果。
# 导包
import threading

# 1.定义全局变量.
global_num = 0


# 2.定义目标函数1，对全局变量累加100W次.
def target_fun1():
    # 2.1 声明为全局变量
    global global_num
    # 2.2 遍历100W次，对全局变量进行累加.
    for i in range(1000000):
        # 2.3 具体的累加动作
        global_num += 1
    # 2.4 累加完毕后，打印结果.
    print(f'target_fun1函数结果：{global_num}')


# 3.定义目标函数2，对全局变量累加100W次.
def target_fun2():
    global global_num
    for i in range(1000000):
        global_num += 1
    print(f'target_fun2函数结果：{global_num}')


# 4.测试.
if __name__ == '__main__':
    # 4.1 创建两个线程，分别关联上述的两个目标函数.
    t1 = threading.Thread(target=target_fun1)
    t2 = threading.Thread(target=target_fun2)

    # 4.2 开启线程.
    t1.start()
    t2.start()
