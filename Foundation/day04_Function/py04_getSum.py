def sum_2_num():
    num1 = 10
    num2 = 20
    result = num1 + num2
    print("%d + %d = %d" % (num1, num2, result))


sum_2_num()


def sum_3_num(n1, n2):
    res = n1 + n2
    print("%d + %d = %d" % (n1, n2, res))


sum_3_num(1, 2)


def sum_4_num(a, b):
    c = a + b
    print("计算结果是 %d" % c)


sum_4_num(5, 6)


def sum_5_num(c, d):
    f = c + d
    return f


g = sum_5_num(4, 5)
print("计算结果是 %d" % g)


def set_param(p, q):
    print(p * q)
    print(p, q)


set_param("a", 20)
