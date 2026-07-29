# 1.导包
import re

# 1. 匹配任意1个字符（除了\n）
# 匹配数据：从左向右匹配，一个字符接着一个字符的匹配
result = re.match("itcast.", "itcast2")

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
