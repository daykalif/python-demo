row = 1
while row <= 5:
    print("*" * row)
    row += 1

rowLine = 1
while rowLine <= 5:
    col = 1
    while col <= rowLine:
        print("*", end="")
        col += 1
    print("")  # 这行代码的目的就是在一行星星输出完成之后，添加换行
    rowLine += 1
