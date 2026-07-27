"""
案例: 装饰器装饰_可变参数

细节:
    装饰器的内部函数格式 要和 被装饰的原函数 保持一致,
    即: 原函数是无参无返回的, 则 装饰器的内部函数也必须是 无参无返回的.
        原函数有参有返回的, 则 装饰器的内部函数必须是 有参有返回的.
"""


# 需求：定义1个可以计算多个数据和字典value值和的函数，并给其友好提示。
# 1. 定义装饰器.
def my_decorator(fn):
    # 1.1 定义内部函数
    def inner(*args, **kwargs):
        # 1.2 额外功能
        print("正在努力计算总和，请稍候...")
        # 1.3 调用原函数
        res = fn(*args, **kwargs)
        # 1.4 返回结果
        return res

    return inner


# 2. 定义原函数.
@my_decorator
def get_sum(*args, **kwargs):
    """
    该函数用于计算 数字元组 和 字典value值 之和.
    :param args: 数字元组, *args → 接收所有的位置参数, 封装到 元组
    :param kwargs: 字典, 键是字符串, 值是数字, **kwargs → 接收所有的关键字参数, 封装到 字典
    :return: 结果之和.
    """
    # 2.1 定义求和变量.
    sum = 0
    # 2.2累加位置参数里所有数字
    for num in args:
        sum += num
    # 2.3累加字典中所有value数值
    for val in kwargs.values():
        sum += val
    # 2.4返回结果
    return sum

    # 上述代码可以优化如下：
    # return sum(args) + sum(kwargs.values())


# 测试调用示例
print(get_sum(1, 2, 3, a=4, b=5, c=6))

print(sum((1, 2, 3)))

my_dict = {
    'a': 3,
    'b': 4,
    'c': 5
}
print(sum(my_dict.values()))
