"""
案例：定义手机类，能开机，关机，拍照。

回顾：
定义类的格式
class 类名:
    # 属性
    # 行为

访问类中成员的格式：
类外：对象名. 的方式
类内：self. 的方式
"""


# 1.定义手机类
class Phone:
    # 属性

    # 行为
    # 1.1 开机
    def open(self):
        print(f'{self} 手机开机了')

    # 1.2 关机
    def close(self):
        print(f'{self} 手机关机了')

    # 1.3 拍照
    def take_photo(self):
        print(f'{self} 手机拍照了')


# 2. 创建手机类对象，访问其成员
p1 = Phone()
print(f'p1对象：{p1}')
p1.open()
p1.take_photo()
p1.close()
print('-' * 34)

# 3.继续创建手机类对象，访问其成员
p2 = Phone()
print(f'p2对象：{p2}')
p2.open()
p2.take_photo()
p2.close()
