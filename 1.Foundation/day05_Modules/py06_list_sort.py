name_list = ["zhangsan", "lisi", "zhangsan", "wangwu"]
num_list = [6, 38, 4, 2, 7, 9]

# 生序
name_list.sort()
num_list.sort()

print(name_list)
print(num_list)

# 降序
name_list.sort(reverse=True)
num_list.sort(reverse=True)

print(name_list)
print(num_list)

# 逆序(反转)
name_list.reverse()
num_list.reverse()

print(name_list)
print(num_list)
