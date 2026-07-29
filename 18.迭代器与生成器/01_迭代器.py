"""
案例：演示自定义迭代器。

迭代器介绍：
    概述:
        自定义的类，只要重写了 __iter__() 和 __next__() 方法，就可以称为 迭代器。
    目的:
        隐藏底层的逻辑，让用户使用更方便。
        惰性加载，用的时候才会获取。

# 回顾：for循环格式
for i in 可迭代类型:
    pass
"""

# 需求：模拟range(1, 6)，自定义 迭代器实现同等逻辑。
# 场景1：回顾 range()用法.
for i in range(1, 6):
    print(i)
print('-' * 23)


# 场景2：自定义迭代器。
# 1. 自定义 迭代器类。
class MyIterator:
    # 2. 通过init魔法方法，初始化属性，指定：范围。
    def __init__(self, start, end):
        self.current_value = start  # 当前值，默认为 开始值。
        self.end = end  # 结束值。

    # 3. 重写iterator魔法方法，返回当前对象(即：迭代器对象)。
    def __iter__(self):
        return self

    # 4. 重写next魔法方法，返回当前值，并更新当前值。

    # 写法一：
    # def __next__(self):
    #     # 4.1 判断当前值范围是否合法。
    #     if self.current_value >= self.end:  # 包左不包右
    #         raise StopIteration  # 抛出异常，迭代结束。
    #     # 4.2 走这里，说明当前值合法，返回当前值，并更新当前值。
    #     value = self.current_value  # value =  1  2  3  4  5
    #     self.current_value += 1  # self.current_value =  2  3  4  5  6
    #     return value

    # 写法二：
    def __next__(self):
        # 4.1 判断当前值范围是否合法。
        if self.current_value >= self.end:  # 包左不包右
            raise StopIteration  # 抛出异常，迭代结束。
        # 4.2 走这里，说明当前值合法，返回当前值，并更新当前值。
        self.current_value += 1
        return self.current_value - 1


if __name__ == '__main__':
    # 5.1 创建迭代器对象，并遍历（for循环）
    for i in MyIterator(start=1, end=6):
        print(i)

    # 5.2 next()函数
    it = MyIterator(10, 13)
    print(next(it))
    print(next(it))
    print(next(it))
    # print(next(it))   # raise StopIteration  # 抛出异常，迭代结束。
