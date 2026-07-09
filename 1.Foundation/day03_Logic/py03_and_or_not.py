age = 12
if age >= 0 and age <= 120:
    print("年龄正确")
else:
    print("年龄不正确")

python_score = 50
c_score = 50
if python_score > 60 or c_score > 60:
    print("考试通过")
else:
    print("考试失败，继续努力")

# 在开发中，通常希望某个条件不满足时，执行一些代码，可以使用not
# 另外，如果需要拼接复杂的逻辑计算跳进啊，同样也有可能使用到not
is_employee = False
if not is_employee:
    print("非公司人员，请勿入内")
