# 1.输入苹果单价
price_str = input("请输入苹果价格：")

# 2.要求苹果重量
weight_str = input("请输入苹果重量：")


# 3.将苹果单价转换成小数
price = float(price_str)
# price = float(input("请输入苹果价格："))

# 4.将苹果重量转换成小数
weight = float(weight_str)

# 5.计算金额
money = price * weight

print(money)
