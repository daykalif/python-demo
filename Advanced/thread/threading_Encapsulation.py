# coding=utf-8
import threading
import time


def sing():
    for i in range(3):
        print("正在唱歌... %d" % i)
        # time.sleep(1)


class MyThread(threading.Thread):

    @staticmethod
    def login(self):
        print("这是登陆...")

    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I am" + self.name + '@' + str(i)  # name属性中保存的是当前线程的名字
            print(msg)
        sing()
        self.login(self)


def main():
    t = MyThread()
    t.start()


if __name__ == '__main__':
    main()
