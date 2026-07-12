name_list = ["zhangsan", "lisi", "zhangsan", "wangwu"]
list_len = len(name_list)
print("列表中包含%d个元素" % list_len)

count = name_list.count("zhangsan")
print("zhangsan出现了%d次" % count)

name_list.remove("lisi")
print(name_list)
