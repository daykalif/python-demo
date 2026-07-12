# 使用迭代遍历列表

# 顺序的从列表中一次获取数据，每一次循环过程中，数据都会保存在my_name
# 这个变量中，在循环体内部可以访问到当前这一次获取到的数据

name_list = ["zhangsan", "lisi", "zhangsan", "wangwu"]
for my_name in name_list:
    print("我的名字叫 %s" % my_name)

# 列表也可以存放不同的数据类型
name = ["nihao", 1, 1.73]
print(name)
