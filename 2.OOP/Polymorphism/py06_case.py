"""
方法综合案例：
    需求：
        1.设计一个Game类
        2.属性：
            1).定义一个类属性top_score记录游戏的历史最高分
            2).定义一个实例属性player_name记录当前游戏的玩家姓名
        3.方法：
            1).静态方法show_help显示游戏帮助信息
            2).类方法show_top_score显示历史最高分
            3).实例方法start_game开始当前玩家的游戏
        4.主程序步骤：
            1).查看帮助信息
            2).查看历史最高分
            3).创建游戏对象，开始游戏


案例小节：
    1.实例方法 -- 方法内部需要访问实例属性 -- 方法内部既需要访问实例属性，又需要访问类属性
        实例方法内部可以使用 类名. 访问类属性
    2.类方法 -- 方法内部只需要访问类属性
    3.静态方法 -- 方法内部，不仅需要访问实例属性和类属性
"""


class Game(object):
    # 类属性top_score记录游戏的历史最高分
    top_score = 0

    # 实例属性player_name记录当前游戏的玩家姓名
    def __init__(self, player_name):
        self.player_name = player_name  # 实例属性player_name定义在__init__中

    # 静态方法show_help显示游戏帮助信息
    @staticmethod
    def show_help():
        print("帮助信息：让僵尸进入大门")

    # 类方法show_top_score显示历史最高分(类方法调用类属性)
    # 类方法就是针对类对象定义的方法：在类方法内部可以直接访问类属性或者调用其他的类方法
    @classmethod
    def show_top_score(cls):
        print("历史记录：%d" % cls.top_score)

    # 实例方法start_game开始当前玩家的游戏
    def start_game(self):
        print("%s 开始游戏啦..." % self.player_name)


# 1.查看游戏的帮助信息
Game.show_help()

# 2.查看历史最高分
Game.show_top_score()

# 3.创建游戏对象，开始游戏
game = Game("小明")
game.start_game()
