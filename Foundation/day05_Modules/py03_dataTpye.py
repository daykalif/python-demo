name_list = ["zhangsan", "lisi", "wangwu"]
print(name_list[1])
print(name_list.index("wangwu"))
name_list[1] = "李四"
name_list.append("王小二")
name_list.insert(1, "你好")
print(name_list)
temp_list = ["孙悟空", "猪八戒", "沙师弟"]
name_list.extend(temp_list)
print(name_list)
name_list.remove("wangwu")
print(name_list)
name_list.pop()  # 删除列表中最后一个元素
print(name_list)
name_list.pop(3)  # 删除指定索引的元素
print(name_list)
name_list.clear()  # 清空列表
print(name_list)
