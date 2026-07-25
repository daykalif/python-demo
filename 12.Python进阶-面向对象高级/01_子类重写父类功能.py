"""
案例：演示子类重写父类功能。

重写解释：
概述：
    重写也叫覆盖，即：子类出现和父类重名的属性 或者 行为，称之为：重写。
调用层次：
    遵循 就近原则，子类有就用，没有就去就近的父类找，依次查找其所有的父类，有就用，没有就报错。
"""


# 故事3：小明掌握了老师傅和黑马的技术后，自己潜心钻研出一套自己的独门配方的全新摊煎饼果子技术。
# 1. 老师父类.
class Master:
    # 1.1 属性
    def __init__(self):
        self.kongfu = '[古法煎饼果子配方]'

    # 1.2 行为
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 2. 黑马学校类
class School:
    # 2.1 属性
    def __init__(self):
        self.kongfu = '[黑马AI煎饼果子配方]'

    # 2.2 行为
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 3. 徒弟类
class Prentice(School, Master):
    # 3.1 属性
    def __init__(self):
        self.kongfu = '[独创煎饼果子配方]'

    # 3.2 行为
    def make_cake(self):
        print(f'运用{self.kongfu}制作煎饼果子')


# 4. 测试.
if __name__ == '__main__':
    # 4.1 创建徒弟类对象.
    p = Prentice()

    # 4.2 访问属性.
    print(p.kongfu)

    # 4.3 调用函数.
    p.make_cake()
