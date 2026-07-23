class Duck:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳...111...')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳...222...')


class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):
        print(f'{self.age} 岁的 {self.name} 正在游泳...333...')


def go_swimming(duck: Duck):
    duck.swimming()


if __name__ == '__main__':
    duck = Duck("小黄鸭", 2)
    dog = Dog("旺财", 3)
    pig = Pig("小猪", 1)

    go_swimming(duck)  # 2 岁的 小黄鸭 正在游泳...111...
    go_swimming(dog)  # 3 岁的 旺财 正在游泳...222...
    go_swimming(pig)  # 1 岁的 小猪 正在游泳...333...
