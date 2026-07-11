"""
Python 里的字典（dict）是一种常用可变容器，核心存储单元是键值对（key: value）：
key（键）：具备唯一性、不可变（可用字符串str、数字int/float、元组tuple等类型，不能用列表这类可变类型）
          充当查找的索引；key不能重复，如果重复，后面的值会覆盖前面的值

value（值）：没有类型和唯一性限制，可以是任意 Python 数据对象；

核心特性：能通过唯一的键快速查询、修改、删除对应的取值，查询效率很高。
"""

"""
一、字典定义与核心概念
字典：使用键值对（key: value）来存储数据，每一个键都对应一个值，通过键（key）可以快速找到对应的值（value）。
特点：键值对（key: value）存储、键（key）不能重复、可修改。


二、字典的定义方式
# 定义字典
字典名称 = {key: value, key:value, key:value ...}
# 示例
dict1 = {"王林": 675, "李慕婉": 608, "许立国": 478, ...}

# 定义空字典
字典名称 = {}
字典名称 = dict()
# 示例
dict2 = {}
dict3 = dict()


三、根据 key 获取 value
# 语法
值 = 字典名称[key]
# 示例
score = dict1["李思"]


四、注意事项
- 字典（dict）中的value 可以是任何类型的数据，而key 不能为可变类型（如：不能为 列表 list、集合 set、字典 dict）。
- 字典内的 key 不允许重复,如果重复定义相同 key，后面的键值对会覆盖前面的
- 字典没有索引下标，不能通过数字索引取值,只能通过 key 来获取对应的 value
"""

# 定义字典
student_dict = {"name": "韩立", "age": 22, "course": ["足球", "艺术"]}
print(type(student_dict))

# 根据键获取值
print(student_dict["name"])  # 输出：韩立
print(student_dict["age"])  # 输出：22

# 修改
student_dict["name"] = "张三"
print(student_dict)

# ------------------------------ 字典 常见操作 ------------------------------

# ------------------------------ 1. 定义字典 ------------------------------
dict1 = {"王林": 670, "李慕婉": 608, "许立国": 580, "韩立": 688}
print("初始字典：", dict1)

# ------------------------------ 2. 添加/修改 ------------------------------
# 添加（key不存在）
dict1["涛哥"] = 550
print("添加后：", dict1)

# 修改（key存在）
dict1["涛哥"] = 620
print("修改后：", dict1)

# ------------------------------ 3. 查询 ------------------------------
# 方式1：直接取值（key不存在会报错）
print("直接取涛哥的成绩：", dict1["涛哥"])
# 方式2：get取值（key不存在返回None，更安全）
print("get取涛哥的成绩：", dict1.get("涛哥"))

# 获取所有key
print("所有key：", dict1.keys())
# 获取所有value
print("所有value：", dict1.values())
# 获取所有键值对
print("所有键值对：", dict1.items())

# ------------------------------ 4. 删除 ------------------------------
# 方式1：pop() 删除并返回value
score = dict1.pop("许立国")
print("被删除的许立国成绩：", score)
print("删除许立国后：", dict1)

# 方式2：del 直接删除（无返回值）
del dict1["韩立"]
print("删除韩立后：", dict1)

# ------------------------------ 5. 遍历 ------------------------------
print("\n--- 遍历方式1：遍历key ---")
for k in dict1.keys():
    print(f"{k} : {dict1[k]}")

print("\n--- 遍历方式2：遍历item元组 ---")
for item in dict1.items():
    print(f"{item[0]} : {item[1]}")

print("\n--- 遍历方式3：直接解包key和value（推荐） ---")
for k, v in dict1.items():
    print(f"{k} : {v}")

# ---------------------------------------------购物车管理系统案例--------------------------------------------------------
"""
需求说明
开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询和统计功能。系统使用嵌套字典结构存储商品数据，通过控制台菜单与用户交互。

具体功能
添加购物车：用户根据提示录入商品名称、价格、数量，保存该商品信息到购物车。
修改购物车：用户输入要修改的商品名称，再录入新的价格和数量，完成后更新该商品信息。
删除购物车：用户输入要删除的商品名称，根据名称删除购物车中的对应商品。
查询购物车：展示购物车中所有商品信息，格式为：商品名称：xxx，商品价格：xxx，商品数量：xxx。
退出购物车：退出系统。
"""

shopping_cart = {}

menu = """
#################### 购物车系统 ####################
#		1. 添加购物车			#
#		2. 修改购物车			#
#		3. 删除购物车			#
#		4. 查询购物车			#
#		5. 退出购物车			#
####################################################
"""

print("欢迎使用购物车管理系统！")

while True:
    # 1.制作菜单
    print(menu)

    # 2.执行的具体操作
    choice = input("请选择要执行的操作（1-5）：")

    match choice:
        case "1":  # 添加购物车
            # 1. 获取用户输入的商品信息
            goods_name = input("请输入商品名称：")
            goods_price = float(input("请输入商品价格："))
            goods_num = int(input("请输入商品数量："))

            # 2. 判断商品是否已存在
            if goods_name in shopping_cart:
                # 商品已存在：提示用户，不执行添加
                print("该商品已存在，请重新选择 ~")
            else:
                # 商品不存在：添加到购物车（嵌套字典结构）
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完毕 ~")
        case "2":  # 修改购物车
            # 1. 获取用户输入的商品信息
            goods_name = input("请输入要修改的商品名称：")
            goods_price = float(input("请输入商品最新的价格："))
            goods_num = int(input("请输入商品最新的数量："))

            # 2. 判断商品是否存在
            if goods_name not in shopping_cart:
                # 商品不存在：提示用户，不执行修改
                print("该商品不存在，请重新选择 ~")
            else:
                # 商品存在：覆盖更新价格和数量
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品修改完毕 ~")
        case "3":  # 删除购物车
            # 1. 获取要删除的商品名称
            goods_name = input("请输入要删除的商品名称：")

            # 2. 判断商品是否存在
            if goods_name not in shopping_cart:
                # 商品不存在：提示错误
                print("该商品不存在，请重新选择 ~")
            else:
                # 商品存在：执行删除
                del shopping_cart[goods_name]
                print("商品删除完毕 ~")
        case "4":  # 查询购物车
            # 遍历购物车中的所有商品名称
            for goods_name in shopping_cart.keys():
                # 获取当前商品的详细信息（价格和数量）
                goods_info = shopping_cart[goods_name]
                # 按要求格式输出商品信息
                print(f"商品名称：{goods_name}，商品价格：{goods_info['price']}，商品数量：{goods_info['num']}")
        case "5":  # 退出购物车
            print("Bye~")
            break
        case _:  # 匹配其他所有情况（默认分支）
            print("非法操作，不支持!!!")
