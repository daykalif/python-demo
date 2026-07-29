import re

# 6 \S 匹配非空白
# 匹配数据
result = re.match("itcast\\S", "itcast\t")

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
