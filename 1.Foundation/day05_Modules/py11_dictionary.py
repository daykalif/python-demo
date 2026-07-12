xiaoming = {
    "name": "小明",
    "age": 19,
    "height": 1.73,
    "gender": True
}

print(xiaoming)

# 取值
print(xiaoming["name"])

# 修改
xiaoming["age"] = 18
xiaoming["weight"] = 120
print(xiaoming)

# 删除
xiaoming.pop("name")
print(xiaoming)

# 统计键值对数量
print(len(xiaoming))

# 合并字典:如果被合并的字典中包含已经存在的键值对，会覆盖原有的键值对
temp_dict_xiaoming = {"height": 1.79, "gae": 30}
xiaoming.update(temp_dict_xiaoming)
print(xiaoming)

# 清空字典
xiaoming.clear()
print(xiaoming)

# 循环遍历字典
xiaoming_dict = {
    "name": "xiaoming",
    "sex": "Male",
    "phone": "10086"
}
for k in xiaoming_dict:
    print("%s - %s" % (k, xiaoming_dict[k]))

# 循环遍历数组字典
card_list = [
    {
        "name": "xiaoming",
        "sex": "Male",
        "phone": "10086"
    },
    {
        "name": "lisi",
        "sex": "Female",
        "phone": "10010"
    }
]

for card_info in card_list:
    print(card_info)
