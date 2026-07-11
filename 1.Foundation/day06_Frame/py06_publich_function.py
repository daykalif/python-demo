a = [1, 2, 3]

del a[1]
print(a)

del (a[1])
print(a)

t_str = "fhakfnznozbvcjxhuwbrbjsfd"
print(max(t_str))
print(min(t_str))

t_list = [34, 1, 4, 74, 7]
print(max(t_list))
print(min(t_list))

t_dict = {
    "a": "z",
    "b": "y",
    "c": "x"
}
print(max(t_dict))  # c
print(min(t_dict))  # a

print("1" > "2")  # False
print("1" < "2")  # True
print("aaa" < "bbb")  # True
print([1, 1, 1] < [2, 2, 2])  # True
print((1, 1, 1) < (2, 2, 2))  # True
# print({"a": "z"} < {"b": "y"})  # 报错,字典不能比较   # python3中取消了cmp
