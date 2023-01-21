import threading
import time

g_num = 0

# 创建一个互斥锁，默认是没有上锁的
mutex = threading.Lock()


def test1(num):
    global g_num
    # 上锁
    mutex.acquire()
    for i in range(num):
        g_num += 1
    # 解锁
    mutex.release()
    print("----in test1 g_num %s-----" % str(g_num))


def test2(num):
    global g_num
    # 上锁
    mutex.acquire()
    for i in range(num):
        g_num += 1
    # 解锁
    mutex.release()
    print("----in test2 g_num %s-----" % str(g_num))


def main():
    t1 = threading.Thread(target=test1, args=(10000000,))
    t2 = threading.Thread(target=test2, args=(10000000,))

    t1.start()
    t2.start()

    time.sleep(2)
    print("-----in main Thread g_num is %s-----" % str(g_num))


if __name__ == '__main__':
    main()
