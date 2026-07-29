import re

# + 匹配前一个字符出现1次或者无限次，即至少有1次
# 数字必须出现1次或者多次
result = re.match("itcast\d+itcast", "itcast11333444itcast")

# 获取数据
if result:
    info = result.group()
    print(info)  
else:
    print("没有匹配到")
