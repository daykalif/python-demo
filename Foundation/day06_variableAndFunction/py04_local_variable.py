def demo1():
    num = 10
    print(num)
    num = 20
    print("修改过后%d" % num)


def demo2():
    num = 100  # 该num与demo1的num没有关系
    print(num)


demo1()
demo2()
print("over")
