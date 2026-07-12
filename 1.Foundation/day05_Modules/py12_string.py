str1 = "我是双引号定义的"
str2 = '我是单引号定义的'
print(str2)
print(str1[6])

for char in str1:
    print(char)

hello_str = "hello abc helloHELLO"
# 统计字符串长度
print(len(hello_str))

# 统计某一个小（子）字符串出现的次数
print(hello_str.count("llo"))
print(hello_str.count("aaa"))

# 某一个子字符串出现的位置
print(hello_str.index("llo"))

# 1.判断空白字符
space_str = "   \t\n\r"
print(space_str.isspace())

# 2.判断字符串中是否只包含数字
num_str = "1"
# 以下3种方法：
#   1>都不能判断小数
#       num_str = "1.1"                     # False False False
#   2>unicode字符串
#       num_str = "(1)"                     # False False False
#       num_str = "\u00b2"  # 数学上的平方    # False True True
#   3>中文数字
#       num_str = "一千零一"                 # False False True

print(num_str)
print(num_str.isdecimal())  # 能判断字符串中是否只包含数字；不能判断小数             # ----常用这个
print(num_str.isdigit())  # 能判断字符串中是否只包含数字，unicode编码；不能判断小数
print(num_str.isnumeric())  # 能判断字符串中是否只包含数字，unicode编码，中文；不能判断小数
