a = 6
b = 100

# 解法1:使用临时变量
c = b
b = a
a = c

# 解法2:不使用临时变量
a = a + b
b = a - b
a = a - b

# 解法3:Python专有,利用元祖
a, b = b, a

print(a)
print(b)
