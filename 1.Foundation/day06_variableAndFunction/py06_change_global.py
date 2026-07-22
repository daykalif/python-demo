num = 10


def demo1():
    print("demo1" + "-" * 50)

    # global关键字，告诉python解释器num是一个全局变量

    global num
    num = 100
    print(num)


def demo2():
    print("demo2" + "-" * 50)
    print(num)


demo1()
demo2()
print("over")
