import time


def task1():
    while True:
        print("----1----")
        time.sleep(0.1)
        yield


def task2():
    while True:
        print("----2----")
        time.sleep(0.1)
        yield


def main():
    t1 = task1()
    t2 = task2()
    # 先让t1运行一会，当t1遇到yield的时候，再返回到24行，然后
    # 执行t2，当它遇到yield的时候，再次切换到t1中，
    # 这样t1/t2/t3的交替运行，最终实现了多任务...协程
    while True:
        next(t1)
        next(t2)


if __name__ == '__main__':
    main()
