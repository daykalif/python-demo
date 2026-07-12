def print_line(char, times):
    # 将鼠标放到函数名上面，黄色灯泡选择Insert documentation...添加参数说明注释
    # 添加完注释之后，将鼠标移到函数名上面（定义的地方，或者调用的地方都可以），
    # 按住快捷键ctrl+q,即可查看说明注释

    """
    打印单行注释
    :param char:
    :param times:
    """
    print(char * times)


def print_lines(char, times):
    """打印多行分割线
    :param char: 分割线使用的分割字符
    :param times: 分割线重复次数
    """
    row = 0
    while row < 5:
        print_line(char, times)
        row += 1


print_lines("-", 20)
