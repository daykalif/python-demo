import re

# 8 \W 匹配特殊字符,即非字母,非数字,非_,非汉字
# 匹配数据
result = re.match("itcast\\W", "itcast\t2aa")

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
