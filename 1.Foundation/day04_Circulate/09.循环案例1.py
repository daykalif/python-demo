"""
案例 1：登录操作
需求说明：根据输入的用户名密码执行登录操作，具体要求如下：
正确的用户名和密码为：admin/666888、zhangsan/123456、taoge/888666
输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
输入的用户名和密码不能为空！
登录成功：输出 "登录成功，进入B站首页~"
登录失败：输出 "用户名或密码错误，请重新输入！"

关键字：
    break：只能够出现在循环中，表示结束、跳出循环的含义（break跳出循环时，while后面的else中的代码将不回执行）
    continue: 只能够出现在循环中，表示中断本次循环，直接进入下一次循环
"""

while True:
    username = input("请输入正确的用户名:")
    password = input("请输入正确的密码:")

    if username == "" or password == "":
        print("输入的用户名或密码不能为空")
        continue

    if username == "admin" and password == "666888":
        print("登录成功")
        break

    elif username == "zhangsan" and password == "123456":
        print("登录成功")
        break

    else:
        print("登录失败")
