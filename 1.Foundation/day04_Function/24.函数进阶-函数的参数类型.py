"""
函数的参数类型

- 普通参数：数字、布尔、字符串、列表、元祖、集合、字典等
- 特殊参数：函数
"""


# 加
def add(x, y):
    return x + y


# 减
def subtract(x, y):
    return x - y


# 乘
def multiply(x, y):
    return x * y


# 除
def divide(x, y):
    return x / y


# 计算
def calc(x, y, oper):
    return oper(x, y)


# 正确调用示例（传入函数名）
result = calc(10, 20, add)
print(result)  # 输出 30
