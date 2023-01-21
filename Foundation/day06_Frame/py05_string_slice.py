# str[索引开始位置,索引结束位置(不包含),步长(步长为-1表示从右往左)]

num_str = "0123456789"
# 1.截取2-5位置的字符串
print(num_str[2:6])

# 2.截取2-9位置的字符串
print(num_str[2:])

# 3.截取0-5位置的字符串
print(num_str[0:6])

# 4.截取全部字符串
print(num_str[:])

# 5.从开始位置,每隔一个字符截取字符串
print(num_str[::2])

# 6.从索引1开始,每隔一个字符截取字符串
print(num_str[1::2])

# 7.截取末尾的字符串
print(num_str[-1])

# 8.截取2～末尾-1的字符串
print(num_str[2:-1])

# 9.截取字符串末尾两个字符
print(num_str[-2:])

# 10.获取字符串的逆序
print(num_str[0::-1])  # 0
print(num_str[-1::-1])  # 9876543210

# 11.数组切片和运算符
lists = [0, 1, 2, 3, 4]
print(lists[1:3])
print(lists * 5)

# 12.元祖切片和运算符
tuples = (0, 1, 2, 3, 4)
print(tuples[1:3])
print(tuples * 5)

# 13.字典切片
dictionary = {
    "a": "aa",
    "b": "bb",
    "c": "cc"
}
# print(dictionary[1:2])    # 报错
# print(dictionary * 5)    # 报错，因为key是唯一的


# 14.字符串拼接
print("hello" + "python")

# 15.数组拼接
print([1, 2] + [3, 4])

t_list = [1, 3]
t_list.extend([2, 4])
print(t_list)
t_list.append(0)
print(t_list)
t_list.append([8, 9])
print(t_list)

# 16.元祖拼接
print((1, 2) + (3, 4))

# 17.in和not in的使用
print("a" in "abcd")  # True
print("e" not in "abcd")  # True
print(1 not in [1, 2, 3])  # False
print(4 not in [1, 2, 3])  # True
print("a" in {"a": "aa"})  # True
