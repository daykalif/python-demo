# 工作日程安排
day = input("请输入星期几(1-7): ")

if day == "1":
    print("周一: 工作会议日")
elif day == "2":
    print("周二: 学习培训日")
elif day == "3":
    print("周三: 项目开发日")
elif day == "4":
    print("周四: 代码审查日")
elif day == "5":
    print("周五: 总结规划日")
elif day == "6" or day == "7":
    print("周末: 休息放松")
else:
    print("输入错误")




# 现代 match-case 写法（Python 3.10+ 新特性）
day = input("请输入星期几(1-7): ")

match day:
    case "1":
        print("周一: 工作会议日")
    case "2":
        print("周二: 学习培训日")
    case "3":
        print("周三: 项目开发日")
    case "4":
        print("周四: 代码审查日")
    case "5":
        print("周五: 总结规划日")
    case "6" | "7":
        print("周末: 休息放松")
    case _:
        print("输入错误")



# ----------------------------------------------------------------------------------
num1 = float(input("请输入第一个数："))
num2 = float(input("请输入第二个数："))
oper = input("请输入运算符(+ - * /)：")

match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/" if num2 != 0:  # 仅当除数不为0时匹配此分支
        print(f"{num1} / {num2} = {num1 / num2}")
    case "/":  # 处理除数为0的情况
        print("错误：除数不能为0！")
    case _:
        print("操作不支持！！！")