import re

# 5 {m,n} 匹配前一个字符出现从m到n次
# 注意1:{2,5} 中括号里面,逗号之后不能加空格
result = re.match("itcast\d{2,5}itcast", "itcast111itcast")
# 获取数据
if result:
    info = result.group()
    print(info)
else:
    print("没有匹配到")
