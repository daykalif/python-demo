def test1():
    print("*" * 30)
    print("test1")
    print("*" * 30)


def test2():
    print("-" * 40)
    test1()
    print("test2")
    print("-" * 40)


test2()
