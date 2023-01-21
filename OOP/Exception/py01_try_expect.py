# try:
#     # 不能确定正确执行的代码
#     num = int(input("请输入一个整数："))
#
# except:
#     # 错误的处理代码
#     print("请输入正确的整数")
#
# print("-" * 50)

try:
    # 提示用户输入一个整数
    number = int(input("请输入一个整数："))
    # 使用8初一用户输入的整数并且输出
    result = 8 / number
except ZeroDivisionError:
    # 针对错误类型1，对代码处理
    print("除0错误")
except (ValueError, '错误类型2', '错误类型3'):
    # 针对ValueError,错误类型2 和 3，对应的代码处理
    print("非整数")
except Exception as result:  # 捕获未知错误
    print("未知错误 %s" % result)
else:
    # 没有异常才会执行的代码
    pass
finally:
    # 无论是否有异常，都会执行的代码
    print("无论是否有异常，都会执行的代码")
