from threading import Thread
import time

g_num = 100


def work1():
    # 全局变量需要重新指向地址，需要使用global
    global g_num
    for i in range(3):
        g_num += 1
    print("-----in work1, g_num is %d-----" % g_num)


def work2():
    # 全局变量不需要重新指向地址，只是使用，不需要使用global
    print("-----in work2, g_num is %d-----" % g_num)


def main():
    print("-----线程创建之前, g_num is %d-----" % g_num)

    t1 = Thread(target=work1)
    t1.start()

    # 延时一会，保证t1线程中的事情做完
    time.sleep(1)

    t2 = Thread(target=work2)
    t2.start()


if __name__ == '__main__':
    main()
