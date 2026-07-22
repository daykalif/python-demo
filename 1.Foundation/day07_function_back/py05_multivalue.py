# 定义支持多值参数的函数
# 有时可能有需要一个函数能够处理的参数个数是不确定的，这个时候，就可以使用多值参数
# python中有两种多值参数：
# 1).参数名前增加一个*，可以接收元祖
# 2).参数名前增加两个*，可以接受字典

# 一般在给多值参数命名时，习惯使用以下两个名字：
# *args -- 存放元祖参数，前面有一个*
# *kwargs -- 存放字典参数，前面有两个*
# args是arguments的缩写，有变量的含义
# kw是keyword的缩写，kwargs可以记忆键值对参数


def demo(num, *nums, **person):
    print(num)
    print(nums)
    print(person)


# demo(1)
demo(1, 2, 3, 4, 5)
demo(1, 2, 3, 4, 5, name="小明", age=18)


# 求和
def sum_numbers(*args):
    num = 0
    # 遍历args元祖顺序求和
    for n in args:
        num += n
    return num


print(sum_numbers(1, 2, 3))
