# 常见数据类型
print("Hello")
print(type("Hello"))    # str

print(type(10))       # int
print(type(3.14))     # float
print(type(True))     # bool
print(type(False))    # bool
print(type(None))     # NoneType

num = -100
print(type(num))  # int

num = -100
# isinstance(数据, 类型) 判断数据是否属于指定类型，返回布尔值True/False
print(isinstance(num, int))    # True，-100是整数int类型
print(isinstance(num, float))  # False，不是浮点型
print(isinstance(num, bool))   # False，不是布尔型


# ----------------------------------------------------------------------------------

# 字符：是文本世界的基本单位，一个字母、一个数字、一个标点符号、一个汉字等都是 1 个字符。

# Python 中字符串有 3 种定义方式：

# 1. 双引号定义（单行字符串）
s1 = "Hello"

# 2. 单引号定义（单行字符串）
s2 = 'It\'s very good'

s4 = "It's very good"

# 3. 三引号定义（支持多行字符串）
s3 = """
尊敬的客户：
感谢您选择我们公司的产品。
我们将会为您竭诚的服务。
祝好 ~
"""


s5 = "\t感谢您选择我们公司的产品。\n\t我们将会为您竭诚的服务。"


print(s1)
print(s2)
print(s3)
print(s4)
print(s5)


# ----------------------------------------------------------------------------------

# 常见转义字符详解
# \'：转义单引号，用于在单引号包裹的字符串里正常输出单引号，示例：
s = 'I\'m a student'
print(s)  # 输出：I'm a student

# \"：转义双引号，用于在双引号包裹的字符串里正常输出双引号，示例：
s = "He said \"hello\""
print(s)  # 输出：He said "hello"

# \n：换行符，让后续内容换到新一行输出，示例：
print("第一行\n第二行")

# \t：制表符，相当于按下 Tab 键，产生一段缩进空格，示例：
print("姓名\t年龄")
print("小明\t18")



# ----------------------------------------------------------------------------------

# 字符串拼接
slogan = "黑马程序员" "成就IT黑马"   # 多个字符串字面量直接写
print(slogan)  # 输出：黑马程序员成就IT黑马


slogan = "黑马程序员" + "成就IT黑马" # + 号拼接
print(slogan)  # 输出：黑马程序员成就IT黑马


s1 = "人生苦短"
s2 = "我用Python"
print("吉多·范罗苏姆：" + s1 + "，" + s2)   # 输出：吉多·范罗苏姆：人生苦短，我用Python

# 注意： + 号可以用来拼接两个字符串，但是无法将字符串与字符串进行拼接（非字符串类型需要转换为字符串类型）

# 方案 1：使用 str() 转换类型
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python、Java"
print("大家好，我是" + name + "，今年" + str(age) + "岁，学习的专业是" + pro + "，爱好 " + hobby)

# 方案 2：使用 f-string（推荐，Python 3.6+）
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python、Java"
print(f"大家好，我是{name}，今年{age}岁，学习的专业是{pro}，爱好 {hobby}")

# 方案 3：使用 format() 方法
name = "涛哥"
age = 18
pro = "软件工程"
hobby = "Python、Java"
print("大家好，我是{}，今年{}岁，学习的专业是{}，爱好 {}".format(name, age, pro, hobby))


# 字符串格式化
# 通过 %占位符 的形式完成字符串和变量的快速拼接。（其中 % 表示我要占位，s 表示将变量转为字符串放入占位的位置）

s1 = "涛哥"
print("大家好，我是%s，欢迎大家进入Python课程的学习" % s1)

s1 = "人生苦短"
s2 = "我用Python"
print("吉多·范罗苏姆：%s，%s" % (s1,s2))    # 注意：前面有多少个占位符（%s），后面就需要有多少个变量 (或数据)，前后数量需要一致。

