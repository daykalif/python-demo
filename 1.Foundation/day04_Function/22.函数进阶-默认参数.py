"""
默认参数（缺省参数）
默认参数也称为缺省参数，用于在定义函数时为参数提供默认值，调用函数时可以不传递有默认值的参数。


核心注意事项
位置要求：默认参数必须放在没有默认值的参数列表的后面，一个函数可以设置多个默认参数。
✅ 正确：def reg_stu(name, age, gender, city='北京'):
❌ 错误：def reg_stu(name, age, city='北京', gender):

值覆盖规则：
调用时如果为默认参数传递了值，则会覆盖默认的参数值；
如果没有传递该参数，则直接使用函数定义时的默认值。
"""


# 定义函数
def reg_stu(name, age, gender="男", city='北京'):
    print(f"注册成功,姓名:{name},年龄:{age},性别:{gender},城市:{city}")
    return {"name": name, "age": age, "gender": gender, "city": city}


# 调用函数（不传递默认参数，使用默认值）
stu = reg_stu("张三", 18, "男")
print(stu)

# 调用函数（传递默认参数，覆盖默认值）
stu = reg_stu("赵四", 22, "女", "深圳")
print(stu)

stu = reg_stu("王五", 24, city="深圳")
print(stu)
