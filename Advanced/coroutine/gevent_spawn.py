# pip3 install gevent

import gevent
import time
from gevent import monkey

# 有耗时操作时需要
monkey.patch_all()  # 将程序中用到的耗时操作的代码，换为gevent中自己实现的模块


def f(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)


print("----1----")
g1 = gevent.spawn(f, 5)  # 创建一个普通的Greenlet对象并切换
print("----2----")
g2 = gevent.spawn(f, 5)
print("----3----")
g3 = gevent.spawn(f, 5)
print("----4----")

# g1.join()
# g2.join()
# g3.join()

gevent.joinall([
    gevent.spawn(f, 5),
    gevent.spawn(f, 10),
    gevent.spawn(f, 7)
])
