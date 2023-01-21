# 元祖和字典的拆包
# 在调用带有多值参数的函数时，如果希望：
# 1).将一个元祖变量，直接传递给args
# 2).将一个字典变量，直接传递给kwargs
# 就可以使用拆包，简化参数的传递，拆包的方式是：
# 在元祖变量前，增加一个*
# 在字典变量前，增加两个*


def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 元祖变量/字典变量
gl_nums = (1, 2, 3)
gl_dict = {"name": "小明", "age": 18}

# demo(gl_nums, gl_dict)

# 拆包语法，简化元祖变量/字典变量的传递
demo(*gl_nums, **gl_dict)

demo(1, 2, 3, name="小明", age=18)
