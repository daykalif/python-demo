import re

# 2 [] 匹配[]中列举的字符
# [a-z] [A-Z] [0-9] [a-zA-Z0-9]
# 匹配数据
result = re.match("itcast[123abc]", "itcast376")

# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
