# ------------------------------ 函数 - 变量的作用域 ------------------------------
# 全局变量：在函数外部 或 函数的内部都是可以访问的；
num = 100


# 定义函数
def circle_area(r):
    # 局部变量：只能在函数内部使用
    pi = 3.14
    area = pi * r * r

    global num
    num = 10000
    print("num = ", num)  # 10000

    return area


# 调用函数
c_area = circle_area(10)
print(c_area)

print("num = ", num)  # 10000
