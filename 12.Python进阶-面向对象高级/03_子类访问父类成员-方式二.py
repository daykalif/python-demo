"""
案例：子类重写父类功能后，继续访问父类功能。

思路:
1. 父类名.父类函数名(self)    精准访问，想找哪个父类，就调哪个父类。
2. super().父类函数名()        只能访问最近的那个父类，有就用，没有就往后继续查找。

注意⚠️：使用super()可以自动查找父类，适合单继承使用，多继承不建议使用
"""


# 故事4: 很多顾客都希望能吃到徒弟做出的有自己独立品牌的煎饼果子，也有黑马配方技术的煎饼果子味道。

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

    # 3.3 调用父类的功能
    def make_old_cake(self):
        super().__init__()
        super().make_cake()

    def make_new_cake(self):
        super().make_cake()


# 4. 测试.
if __name__ == '__main__':
    # 4.1 创建徒弟类对象.
    p = Prentice()

    # 4.2 访问属性.
    print(p.kongfu)  # 独创煎饼果子配方
    print('-' * 50)

    # 4.3 调用函数.
    p.make_cake()  # 独创煎饼果子配方
    print('*' * 34)

    p.make_old_cake()  # 黑马AI煎饼果子配方
    print('#' * 34)

    p.make_new_cake()  # 黑马AI煎饼果子配方
    print('*' * 34)

    p.make_cake()  # 黑马AI煎饼果子配方
