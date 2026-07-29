import re

# 1 * 匹配前一个字符出现0次或者无限次，即可有可无
result = re.match("itcast1*", "itcast111123333itcast")  # 1出现0次或者多次
# result = re.match("itcast\d*", "itcast23333itcast")        # 数字出现0次或者多次
# result = re.match("itcast\d*itcast", "itcast123333itcast") # 数字出现0次或者多次 itcast开始 itcast结束
# result = re.match("itcast\d*itcast", "itcastitcast")        # 数字出现0次或者多次 itcast开始 itcast结束

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
