

# 字面量：指程序中，直接书写的固定值（数据），就称字面量
# 1. 字面量的种类
# 2.字面量的书写格式
print(100)  # 整数（int）
print(3.14) # 浮点数/小数（float）
print(True) # 布尔（bool）
print(False) # 布尔（bool）
print("Hello Python") # 字符串（str）,可用双引号
print('------------') # 字符串（str）,也可用单引号
print(None) # 空值（NoneType）

# 布尔类型本质也是整数类型（True -- 1；Flase -- 0）
print(True + 1) # 2
print(False - 1) # -1


# 变量 ---> Python是动态类型语言，一个变量是可以存储不同类型的数据的（但是项目开发中，推荐变量只存储一种类型的数据）
num = 1114.1
print(num)

num = num + 1
print(num)

num = "OK"
print(num)


# 案例
base = 20.7  # 基础播放量
incr = 50    # 每一个月的新增播放量
print("未来第一个月的播放总量：", base + incr)
print("未来第二个月的播放总量：", base + incr + incr)

# 案例 - 升级：一次性可以定义多个变量
base, incr = 20.7, 50
print("未来第一个月的播放总量：", base + incr)
print("未来第二个月的播放总量：", base + incr + incr)



# ---
a = 10
b = 20
c = a  # 把a原本的10存入临时变量c，此时c=10
a = b  # 把b的20赋值给a，此时a=20
b = c  # 把c保存的原a值10赋值给b，此时b=10
print(a, b)
# ---
a = 10
b = 20
a, b = b, a
print(a, b)  # 同样输出20 10