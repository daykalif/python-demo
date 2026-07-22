"""
可变和不可变类型
1).不可变类型，内存中的数据不允许被修改：
数字类型：int,bool,float,complex,long(2.x)
字符串str
元祖tuple

2).可变类型，内存中的数据可以被修改：
列表list
字典dict

注意：字典的key只能使用不可变类型的数据
"""

a = 1
a = "hello"
a = [1, 2, 3]
a = [3, 2, 1]

# --------使用方法，地址不会发生变化；使用赋值，地址发生变化-------------

a = [1, 2, 3]
print(id(a))

a.append(999)
print(id(a))

a.remove(2)
print(id(a))

a.clear()
print(id(a))

a = []
print(id(a))

print('*' * 50)
d = {"name": "zhangsan"}
print(id(d))

d["age"] = 18
print(id(d))

d.pop("age")
print(id(d))

d.clear()
print(id(d))

d = {}
print(id(d))

# 在python中，设置字典的键值对时，会首先对key进行hash已决定如何在内存中保存字典的数据，以方便后续对字典操作：增删改查
print(hash(1))
print(hash("hello"))
print(hash("hello1"))
print(hash((1,)))
# print(hash([]))  # 报错
