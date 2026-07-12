"""
匿名函数
匿名函数指的是没有名称的函数，需要通过lambda表达式来声明函数，可以简化简单函数的编写（单行表达式）。

"""

# ---------------------------- 定义命名函数 ----------------------------
"""
def 函数名(参数列表):
    函数体...
"""


def out_line():
    print('-------------------------')


def add(x, y):
    return x + y


out_line()
print(add(10, 20))

# ---------------------------- 定义匿名函数 ----------------------------
# lambda 参数列表 : 函数体

# 需求1: 打印分隔线
out_line2 = lambda: print('-------------------------')

# 需求2: 计算两个数之和
add = lambda x, y: x + y

out_line2()
print(add(100, 200))

# 需求3：按照每一个元素的字符个数，从小到大排序
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print("原列表：", data_list)

data_list.sort()
print("默认排序后：", data_list)

# key=len 表示以字符串长度作为排序依据
data_list.sort(key=len)
print("按字符数升序后：", data_list)

data_list.sort(key=lambda item: len(item), reverse=True)
print("使用匿名函数排序：", data_list)

"""
1. 匿名函数的定义方式
匿名函数通过 lambda 表达式定义，语法格式为：

# 定义匿名函数
lambda 参数列表 : 函数体

lambda：关键字，用于声明匿名函数
参数列表：可接收多个参数（与普通函数一致）
函数体：单行表达式，执行结果即为返回值（无需写 return）


2. 命名函数与匿名函数的选择
建议使用匿名函数的情况：
函数逻辑简单，仅在一个地方调用（常作为高阶函数的参数，比如 sorted、map 的 key 参数），追求代码简洁。
建议使用命名函数的情况：
函数逻辑复杂，需要多步操作，需要在多个地方重复使用，或者需要添加文档说明、便于维护的场景。

代码的可读性和可维护性比简洁性更重要
"""
