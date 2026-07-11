# 字符串 基本操作 ---> 不可变的(无法修改)、有序性、可迭代性
s = "Hello-Python"

print(s[4])  # 正向索引
print(s[-8])  # 反向索引

for i in s:
    print(i)

# 切片
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[6:12:1])
print(s[6::1])

print("---------------------------")

# 步长 ---> 正数: 从前往后截取 ; 负数: 从后往前截取
print(s[-1:-7:-1])
print(s[::-1])

# ---------------------------------------------------------------------------------------------------------

"""
字符串本身不可变："1" 这个对象一旦生成，永远改不了里面的字符，你没法写成 s[0] = "3" 去修改 "1" 内部内容。
变量可以随便改指向：变量s只是一个 “标签”，它可以解绑旧字符串、绑定全新的字符串，这是完全合法的操作。
"""

s = "1"
# ① 内存里创建字符串对象 "1"
# ② 变量 s 贴在 "1" 这个对象上

s = "2"
# ① 内存里新建字符串对象 "2"
# ② 变量 s 撕掉原来的标签，重新贴到 "2" 身上

print(s)  # 输出 2

# 对比：真正修改字符串内部会报错
# s = "1"
# s[0] = "9"  # 报错！TypeError: 'str' object does not support item assignment

# ------------------------------ 字符串常用方法 ------------------------------
s = "   Hello-Python-Hello-World    "

# find() 查找指定字符串第一次出现的索引位置
index = s.find("-")
print(index)

# count() 统计子字符串在指定字符串中出现的次数
c = s.count("o")
print(c)

# upper() 转为大写
su = s.upper()
print(su)

# lower() 转为小写
sl = s.lower()
print(sl)

# split() 将字符串按照指定字符串切割 - 列表
slist = s.split("-")
print(slist)

# strip() 去除字符串两端的空格
ss = s.strip()
print(ss)

# replace() 将字符串中的指定子串替换为新的内容
sr = s.replace("-", "*")
print(sr)

# startswith() / endswith() 判断字符串是否是以指定的字符串开头 / 结尾，返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))

print(s)  # 原始字符串不会变

# ------------------------------ 字符串案例 ------------------------------
# 案例1: 邮箱格式验证: 用户输入一个邮箱, 验证邮箱格式是否正确(包含一个@和至少一个.), 如果输入正确, 输出"邮箱格式正确", 否则输出"邮箱格式错误"。

# 1. 接收用户输入的邮箱
mail = input("请输入邮箱: ")

# 2. 判断邮箱的格式
if mail.count("@") == 1 and mail.count(".") >= 1:
    print(f"{mail} 是合法的邮箱")
else:
    print(f"{mail} 是非法的邮箱")

# 方式二: in 运算符 ---> 判断子串是否存在字符串中, 存在, 返回True; 否则, 返回False

# 1. 接收用户输入的邮箱
mail = input("请输入邮箱: ")

# 2. 判断邮箱的格式
if mail.count("@") == 1 and "." in mail:
    print(f"{mail} 是合法的邮箱")
else:
    print(f"{mail} 是非法的邮箱")
