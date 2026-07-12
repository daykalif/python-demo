"""
不定长参数 - 位置传递（*args）
不定长位置参数 *args 用于接收任意数量的位置参数，并将其封装为一个元组（tuple）。


核心知识点
参数封装：所有传入的位置参数会被 *args 收集并封装为元组，可直接对 args 使用 min()、max()、sum() 等元组操作。
变量名约定：args 是约定俗成的变量名，并非 Python 关键字，也可使用其他合法名称（如 *data）。
参数范围：*args 只接收位置参数，不接收关键字参数。
灵活调用：函数调用时可传入任意数量的位置参数，无需提前定义参数个数。

"""


# ----------------------------------- 函数 - 不定长参数（位置参数 *args --> 元祖） --------------------------------------------------
# 定义函数
def calc_data(*args):
    print(f"args-------------------->", args)
    print(f"*args===================>", *args)

    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data, max_data, round(avg_data, 1)


# 调用函数
data = calc_data(10, 20, 30, 40, 50, 60, 70, 80, 90, 100)
print(data)

data = calc_data(100, 200, 300, 400, 500)
print(data)

# ----------------------------------- 函数 - 不定长参数（关键字参数 **kwargs --> 字典） --------------------------------------------

"""
不定长参数 - 关键字传递（**kwargs）
不定长关键字参数 **kwargs 用于接收任意数量的关键字参数，并将其封装为一个字典（dict）。


核心知识点
参数封装：所有传入的 键=值 形式的关键字参数会被 **kwargs 收集并封装为字典，可通过 kwargs.get('键名') 读取对应值。
变量名约定：kwargs 是约定俗成的变量名，并非 Python 关键字，也可使用其他合法名称（如 **options、**config）。
混合使用：*args 与 **kwargs 可同时使用，*args 必须在 **kwargs 之前，分别接收位置参数和关键字参数。
灵活扩展：可在不修改函数定义的情况下，通过额外的关键字参数扩展功能（如本例中通过 round 控制平均值精度）。

"""


# 定义函数
def calc_data(*args, **kwargs):
    print(f"args--------------------->", args)

    print(f"kwargs--------------------->", kwargs)
    print(f"*kwargs====================>", *kwargs)

    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)

    if kwargs.get('round'):
        avg_data = round(avg_data, kwargs.get('round'))

    return min_data, max_data, avg_data


# 调用函数
data = calc_data(100, 200, 300, 400, round=2, count=0)
print(data)

data = calc_data(33, 11, 28, 91, 32, 75, 49)
print(data)


"""
小结：

1．什么是不定长参数？
参数个数不确定，此时就可以使用不定长参数解决这类问题

2．不定长参数的分类？
*args：不定长位置参数，函数调用时，通过位置参数传递多个参数封装到一个元组 (tuple) 中
**kwargs：不定长关键字参数，函数调用时，通过关键字参数传递多个参数封装到一个字典 (dict)

3．*args与**kwargs的应用场景？
def calc_data(*args, **kwargs):
*args适用于处理数量不确定的数据
**kwargs适用于处理数量不确定的选项（函数的配置参数，用来定制函数的行为）
"""