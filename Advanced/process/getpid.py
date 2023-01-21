import multiprocessing
import os
import time

"""
线程是操作系统资源分配的单位，线程是操作系统调度的单位
线程依赖于进程，先有进程才有线程
不同：
1.进程不支持资源共享，不共享全局变量
2.进程的资源占用空间大，线程资源占用少
3.父进程结束，子进程不会结束
4.父线程结束，子线程会结束
相同：
5.父进程和父线程的子进程或子线程结束后都会结束
"""

nums = [11, 22, 33]


def test(a, b, c, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(*args)
    print(kwargs)
    nums.append(44)
    print("在子进程1中nums=%s" % str(nums))
    time.sleep(3)

    # while True:
    #     print("----in 子进程 pid=%d,父进程的pid=%d----" % (os.getpid(), os.getppid()))
    #     time.sleep(1)


def test2():
    print("在子进程2中nums=%s" % str(nums))

    # while True:
    #     print("----in 子进程2 pid=%d,父进程的pid=%d----" % (os.getpid(), os.getppid()))
    #     time.sleep(1)


def main():
    print("----in 父进程 pid=%d,父进程的pid=%d----" % (os.getpid(), os.getppid()))
    p = multiprocessing.Process(target=test, args=(11, 22, 33, 44, 55, 66, 77), kwargs={"mm": 11})
    p.start()

    # time.sleep(1)
    p.join()

    p2 = multiprocessing.Process(target=test2)
    p2.start()


if __name__ == '__main__':
    main()
