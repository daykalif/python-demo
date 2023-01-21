import threading
import time

g_nums = [11, 22]


def test1():
    g_nums.append(33)
    print("----in test1 g_nums %s-----" % str(g_nums))


def test2(temp):
    temp.append(44)
    print("----in test2 g_nums %s-----" % str(temp))


def main():
    # target指定将来这个线程去哪个函数执行代码
    # args指定将来调用函数的时候传递什么数据过去
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2, args=(g_nums,))

    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("-----in main Thread g_nums is %s-----" % str(g_nums))


if __name__ == '__main__':
    main()
