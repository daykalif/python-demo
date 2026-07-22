def test(num):
    print("-" * 50)
    print("%d 在函数内的内存地址是 %x" % (num, id(num)))

    result = 100
    print("返回值 %d 在内存中的地址是 %x" % (result, id(result)))

    # 定义一个字符串变量
    res = "hello"
    print("返回值 %s 在内存中的字符串地址是 %x" % (res, id(res)))

    print("-" * 50)
    # 将字符串变量返回
    return result


# 1.定义一个数字的变量
a = 10

# 数据的地址本质上就是一个数字
print("调用函数前的内存地址是 %x" % id(a))

# 2.调用test函数，本质上传递的是实参保存数据的引用，而不是实参
# 注意：如果程序有返回值，但是没有定义变量接收，
# 程序不会报错，但是无法保存获取返回结果
r = test(a)
print("调用函数后实参的内存地址是 %x" % id(a))
print("调用函数后返回值内存地址是 %x" % id(r))
