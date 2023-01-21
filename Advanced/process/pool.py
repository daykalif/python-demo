import os
import random
import time
from multiprocessing import Pool

"""主进程结束后，线程池中所有的线程都会关闭"""


def worker(msg):
    t_start = time.time()
    print("%s开始执行，线程号为%d" % (msg, os.getpid()))
    # random.random()随机生成0-1之间的浮点数
    time.sleep(random.random() * 2)
    t_stop = time.time()
    print(msg, "执行完毕，耗时%0.2f" % (t_stop - t_start))


def main():
    po = Pool(3)
    for i in range(0, 10):
        # Pool().apply_async(要调用的目标，（传递给目标的参数元组，））
        # 每次循环将会用空闲出来的子进程去调用目标
        po.apply_async(worker, (i,))

    print("-----start-----")
    po.close()  # 关闭进程池，关闭po不再接收新的请求
    po.join()  # 等待po中所有子进程执行完成，必须放在close语句之后
    print("-----end-----")


if __name__ == '__main__':
    main()
