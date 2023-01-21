# 格式化字符：
#   %s      字符串
#   %d      有符号十进制数，%06d表示输出的整数显示位数，不足的地方使用0补全
#   %f      浮点数，%.02f表示小数点后只显示两位
#   %%      输出%
name = "大明"
print("我的名字叫：%s，请多多关照" % name)

student_no = 100
print("我的学号是：%06d" % student_no)

price = 8.5
weight = 7.5
money = price * weight
print("苹果单价：%.2f 元/斤，购买了：%.3f 斤，需要支付：%.2f 元" % (price, weight, money))

scale = 0.25
print("数据比例是：%f%%" % scale * 10)    #字符串重复10次输出
print("数据比例是：%.2f%%" % (scale * 100))
