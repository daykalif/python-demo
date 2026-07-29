import re

# ? 匹配前一个字符出现1次或者0次，即要么有1次，要么没有
# 数字出现0次或者1次
result = re.match("itcast\d?itcast", "itcastitcast")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
