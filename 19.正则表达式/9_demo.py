import re

# 4 \D 匹配非数字, 即不是数字
# 匹配数据
result = re.match("itcast\\D", "itcast-")

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
