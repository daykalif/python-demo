"""
单例 -- 让类创建的对象，在系统中只有唯一的一个实例
1.定义一个类属性，初始值是None,用于记录单例对象的引用
2.重写__new__方法
3.如果类属性is None,调用父类方法分配空间，并在类属性中记录结果
4.返回类属性中记录的对象引用
"""

"""
只执行一次初始化工作：
在每次使用类名()创建对象时，python的解释器都会自动调用两个方法：
    __new__分配空间
    __init__对象初始化
在对__new__方法改造之后，每次都会得到第一次被创建对象的引用
但是：初始化方法还会被再次调用

需求：
    让初始化动作只被执行一次
    
解决办法：
    1.定义一个类属性init_flag标记是否执行过初始化动作，初始值为False
    2.在__init__方法中，判断init_flag,如果为False就执行初始化动作
    3.然后将init_flag设置为True
    4.这样，再次自动调用__init__方法时，初始化动作就不会被再次执行了
"""


class MusicPlayer(object):
    # 记录第一个被创建对象的引用,（类属性）
    instance = None
    # 记录是否执行过初始化动作
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 1.判断类属性是否是空对象
        if cls.instance is None:
            # 2.调用父类的方法，为第一个对象分配空间
            cls.instance = super().__new__(cls)

        # 3.返回类属性保存的对象引用
        return cls.instance

    def __init__(self):
        # 1.判断是否执行过初始化动作
        if MusicPlayer.init_flag:
            return

            # 2.如果没有执行过，在执行初始化动作
        print("初始化播放器")

        # 3.修改类属性的标记
        MusicPlayer.init_flag = True


# 创建多个对象
player1 = MusicPlayer()
print(player1)

player2 = MusicPlayer()
print(player2)
