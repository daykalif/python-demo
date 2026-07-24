"""
减肥案例

需求：
例如，小明同学当前体重是 100kg。每当他跑步一次时，则会减少 0.5kg；每当他大吃大喝一次时，则会增加 2kg。请试着采用面向对象方式完成案例。

分析：
类名:　　　Student
对象名:　　xm
属性 (名词): 当前体重，current\_weight
行为 (动词) 跑步，吃饭
"""


# 1.定义学生类.
class Student:
    # 2.在魔法方法init中，完成：对象的属性的初始化.
    def __init__(self):
        self.current_weight = 100

    # 3.每当他跑步一次时，则会减少0.5kg
    def run(self):
        print('疯狂跑步...')
        self.current_weight -= 0.5  # 体重减小.

    # 4.大吃大喝.
    def eat(self):
        print('大吃大喝一顿...')
        self.current_weight += 2

    # 5.重写魔法方法str，打印属性值，即：当前体重.
    def __str__(self):
        # return '当前体重：%s' % self.current_weight
        return f'当前体重：{self.current_weight} kg!'


# 6.测试.
if __name__ == '__main__':
    # 6.1 创建学生对象.
    xm = Student()

    # 6.2 跑步
    xm.run()
    xm.run()

    # 6.3 吃喝
    xm.eat()

    # 6.4 当前体重.
    print(xm)
