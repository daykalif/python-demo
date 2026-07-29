import re

# 3 \d 匹配数字,即0-9 => [0123456789] => [0-9]
# 匹配数据
result = re.match("itcast\\d", "itcast5")

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
