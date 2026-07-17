# 异常处理
try:
    print('----------------------')
    # print(my_name)
    # print(1 / 0)
    # print("ABC"[10])
    print("ABC".hello)
    print('----------------------')
except NameError as e:  # 捕获的是 NameError 类型的异常
    print("名字不存在，请检查变量或函数名字 : 异常信息：", e)
except ZeroDivisionError as e:  # 捕获的是 ZeroDivisionError 类型的异常
    print("0不能做被除数 : 异常信息：", e)
except IndexError as e:  # 捕获的是 IndexError 类型的异常
    print("索引错误 : 异常信息：", e)
except Exception as e:  # 捕获所有异常
    print("程序运行出错了，请联系管理员～ : 异常信息：", e)
finally:  # 无论程序是否正常运行，finally代码块中的所有代码都会运行
    print("释放资源～")


# ---------------------------------------------------
def fun1():
    print("fun1 ... running ...")
    fun2()


def fun2():
    print("fun2 ... running ...")
    fun3()


def fun3():
    print("fun3 ... running ...")
    print(my_color)


if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print("程序运行出错了，请联系管理员～ : 异常信息：", e)
