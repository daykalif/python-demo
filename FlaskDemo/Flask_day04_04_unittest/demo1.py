def div(num1, num2):
    assert isinstance(num1, int), "值类型不正确"
    assert isinstance(num2, int), "值类型不正确"
    assert num2 != 0, "除数不能为0"
    return num1 / num2


if __name__ == '__main__':
    # print(div(100, "hh"))
    print(div(100, 0))
