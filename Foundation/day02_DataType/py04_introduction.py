# 断点调试

# 在运行的时候，Python解释器，会根据赋值语句等号右侧的数据自动推导出变量中保存数据的准确类型
# 数字型
# int表示是一个整数类型
age = 18

# bool表示是一个布尔类型，真True或者假False
age = True

# float表示是一个小数类型，浮点数
height = 1.75

weight = 75.0

# complex 复数型


# 非数字型
# str表示是一个字符串类型
name = "小明"
print(type(name))
# 列表
# 元祖
# 字典

print(type(2 ** 32))
print(type(2 ** 64))  # 在python2.0中，区分int型和Long型，在python3.0中，只有int型

first_name = '张'
last_name = '三'
print(first_name * 10 + last_name)

password = input("请输入银行密码")
print(password, '输出')

int("123")  # 这是整数 <class 'int'>
print(type(int("123")))

float("12.3")   # 这是小数 <class 'float'>
print(type(float("12.3")))
