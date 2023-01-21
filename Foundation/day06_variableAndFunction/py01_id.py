# 引用
a = 1
print(id(a))  # id用来查看变量保存的地址
print(id(1))
b = a
print(id(b))
a = 2
print(id(a))
print(id(b))
