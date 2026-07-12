"""
函数的参数与返回值
在定义函数时，根据业务需要，可以指定参数与返回值，具体格式如下：

# 定义函数
def 函数名(参数列表):
    函数体
    ......
    return 返回值

# 调用函数
函数名(参数)

注意 1： 函数定义时如果有多个参数，多个参数之间使用逗号（,）分隔。
注意 2： return语句只有返回功能，而没有输出打印的功能，如果要输出，需要结合print()函数来实现。
"""


# 函数1: 计算圆的面积
def circle_area(r):
    area = 3.14 * r * r
    return area


# 调用函数
c_area = circle_area(10)
print(c_area)


# 函数2：计算长方形的面积 -- 长，宽
def rectangle_area(l, w):
    area = l * w
    return area


print(rectangle_area(20, 10))


# 函数3：计算圆的面积，周长 -- 半径
# 如果返回值有多个，多个返回值之间逗号分隔 ---> 多个返回值会封装到元组之中
# round() 是 Python 内置的数字四舍五入函数，用于对浮点数进行指定精度的舍入。 第一个参数：要舍入的数字（整数或浮点数），第二个参数：可选参数，保留的小数位数（默认 None，即舍入到整数）
def circle_area_len(r):
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)


# 用法1：用单个变量接收，得到元组
al = circle_area_len(10)
print(al)
print(type(al))

# 用法2：解包，用多个变量分别接收返回值
area, length = circle_area_len(10)  # 不建议用len做变量名，len是Python内置函数名
print(area)
print(length)


# ---------------------------函数说明文档------------------------------------
def circle_calc(r):
    """
    该函数用于根据圆的半径，计算圆的面积和圆的周长
    :param r: 圆的半径
    :return: 圆的面积 ，圆的周长
    """
    pi = 3.14
    area = pi * r ** 2
    perimeter = 2 * pi * r
    return area, perimeter


# 调用示例
area_result, perimeter_result = circle_calc(10)
print("圆的面积：", area_result)
print("圆的周长：", perimeter_result)
