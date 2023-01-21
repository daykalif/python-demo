num = 10


def demo1():
    print("demo1" + "-" * 50)

    # 只是定义了一个局部变量，不会修改到全局变量，只是变量名相同而已

    num = 100
    print(num)


def demo2():
    print("demo2" + "-" * 50)
    print(num)


demo1()
demo2()
print("over")
