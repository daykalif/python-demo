# import可以导入工具包，random是随机数工具包
import random

player = int(input("请输入你要出的拳 石头1/剪刀2/布3:"))
# 输入random加一个小数点可以查看工具包里类型，randint为整型随机数工具包
# 选择randint后在其后加小括号里面可以写产生的随机数的范围，即数学中开区间表示
computer = random.randint(1, 3)
print("玩家出的是%d,电脑出的是%d" % (player, computer))
if (player == 1 and computer == 2) or (player == 2 and computer == 3) or (player == 3 and computer == 1):
    print("哇哦，电脑弱爆了！")
elif player == computer:
    print("真是心有灵犀，再来一次")
else:
    print("不服气，再来~")
