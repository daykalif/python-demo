import re

# 7 \w 匹配非特殊字符，即a-z, A-Z, 0-9, _, 汉字
# 匹配数据
result = re.match("itcast\\w", "itcasta")
# result = re.match("itcast\\w", "itcast!")

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
 