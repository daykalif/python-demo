# 求0-100的和
result = 0
i = 0
while i <= 100:
    print(i)
    result += i
    i += 1
print("0~100之间的数字求和结果 = %d" % result)


# 求0-100之间偶数的和
total = 0
k = 0
while k <= 100:
    if k % 2 == 0:
        print(k)
        total += k
    k += 1
print("0~100之间的偶数数字求和结果 = %d" % total)
