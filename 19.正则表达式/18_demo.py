import re

# 4 {m} 匹配前一个字符出现m次
result = re.match("itcast\d{2}itcast", "itcast12itcast")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
