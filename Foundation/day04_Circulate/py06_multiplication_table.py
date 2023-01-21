# 转义字符
print("1\t2\t3")  # \t制表符
print("10\t20\t30")
print("hello\n python")  # \n换行
print("he\"l\"lo")  # \"输出双引号

row = 1
while row <= 9:
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col, row, col * row), end="\t")
        col += 1
    print("")
    row += 1
