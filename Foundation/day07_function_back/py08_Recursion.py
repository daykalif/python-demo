# 递归：一个函数内部调用自己
def sum_numbers(num):
    print(num)
    # 递归的出口很重要，否则会出现死循环
    if num == 1:
        return
    sum_numbers(num - 1)


sum_numbers(3)


# 递归案例--计算数字累加：1+2+3...+num
def sum_numbers(num):
    if num == 1:
        return 1

    # 假设 sum_numbers 能够完成 num - 1 的累加
    temp = sum_numbers(num - 1)

    # 函数内部的核心算法就是两个数字的相加
    return num + temp


print(sum_numbers(3))
