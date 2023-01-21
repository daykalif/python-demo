# 缺省参数
# 定义函数时，可以给某个参数指定一个默认值，具有默认值的参数就叫做缺省参数
# 调用函数时，入股没有传入缺省参数的值，则函数内部使用定义函数时指定的参数默认值
# 函数的缺省参数，将常见的值设置为参数的缺省值，从而简化函数的调用

gl_num_list = [6, 3, 9]
# 默认就是生序降序，因为这种应用需求更多
gl_num_list.sort()
print(gl_num_list)

# 只有当需要降序排序时，才需要传递`reverse`参数
gl_num_list.sort(reverse=True)
print(gl_num_list)


# 指定函数的缺省参数
# 在参数后使用赋值语句，可以指定参数的缺省值
# 1).缺省参数的定义位置：必须保证带有默认值的缺省参数在参数列表末尾
# 2).在调用函数时，如果有多个缺省参数，需要指定函数名，这样解释器才能够知道参数的对应关系！
def print_into(name, age, gender=True):
    gender_text = "男生"
    if not gender:
        gender_text = "女生"
    print("%s 是 %s,今年 %d 岁" % (name, gender_text, age))


# 假设班上的同学，男生居多！
# 提示：在指定缺省参数的默认值时，应该使用最常见的值作为默认值
print_into("张三", 18)
print_into("李四", 19)
print_into("小美", 17, False)
print_into("小美", 14, gender=False)
