# 定义函数
def reg_stu(name, age, gender, city):
    print(f"注册成功，姓名：{name}，年龄：{age}，性别：{gender}，城市：{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}


# 传参方式一：位置参数（按定义顺序传参）
stu = reg_stu("张三", 18, "男", "北京")
print(stu)

# 传参方式二：关键字参数（指定参数名传参，顺序可任意）
stu = reg_stu(name="王林", age=28, gender="男", city="北京")
print(stu)

stu = reg_stu(age=20, gender="女", city="北京", name="李慕婉")
print(stu)

# 传参方式三：位置参数 + 关键字参数（位置参数必须在前，关键字参数在后）
stu = reg_stu("李慕婉", 20, gender="女", city="北京")
print(stu)
