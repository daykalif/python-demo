import re

# 5 \s 匹配空白,即空格,tab键
# 匹配数据
result = re.match("itcast\\s111", "itcast\t111")

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
