"""
__new__方法：
使用类名()创建对象时，python的解释器首先会调用__new__方法为对象分配空间

__new__是一个由object基类提供的内置的静态方法，主要作用有两个：
    1).在内存中为对象分配空间
    2).返回对象的引用

python的解释器获得对象的引用后，将引用作为第一个参数，传递给__init__方法

__init_ 作用：
    1).对象初始化
    2).定义实例属性

重写__new__方法的代码非常固定！
重写__new__方法一定要return super().__new__(cls)
否则python的解释器得不到分配了空间的对象引用，就不会调用对象的初始化方法
注意：__new__是一个静态放啊，在调用时需要主动传递cls参数
"""


class MusicPlayer(object):
    def __new__(cls, *args, **kwargs):
        # 1.创建对象时，__new__方法会被自动调用
        print("创建对象，分配空间")

        # 2.为对象分配空间,super()是为了调用父类的方法
        # __new__方法是静态方法，需要传递cls参数
        instance = super().__new__(cls)

        # 3.返回对象的引用
        return instance

    def __init__(self):
        print("播放器初始化")


# 创建播放器对象
player = MusicPlayer()
print(player)
