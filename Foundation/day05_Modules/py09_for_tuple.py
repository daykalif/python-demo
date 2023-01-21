info_tuple = ("zhangsan", 18, 1.75)
for my_info in info_tuple:
    print(my_info)  # 元祖中保存的数据类型通常是不同的，所以不经常使用循环遍历

"""
    元祖的应用场景：
        1).函数的参数和返回值，一个函数可以接收任意多个参数，或者一次返回多个数据
        2).格式字符串，格式化字符串后面的()本质上就是一个元祖
        3).让列表不可以被修改，以保护数据安全
"""

print("%s 年龄是 %d 身高是 %.2f" % ("zhangsan", 18, 1.75))
print("%s 年龄是 %d 身高是 %.2f" % info_tuple)

info_str = "%s 年龄是 %d 身高是 %.2f" % info_tuple
print(info_str)
