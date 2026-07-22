#! /usr/bin/python3

"""
# 终端运行：which python3   -->  /usr/bin/python3

# Linux 上的 Shebang 符号(#!)
#! 必须连接在一起
#! 一句必须在文件的最开始，第一行
# 开头的语句一般情况下会被当成注释而忽略，所以Shebang 对文件的内容是没有影响的
#! 开头的一行会设置解释器运行环境
"""

from Foundation.day06_VisitingCard import cards_tools

# 无限循环，由用户主动决定什么时候退出循环！
while True:
    # TODO(daykalif) 显示功能菜单
    cards_tools.show_menu()

    action_str = input("请选择希望执行的操作：")
    print("您选择的操作是【%s】" % action_str)

    # 1,2,3针对名片的操作
    if action_str in ["1", "2", "3"]:
        # 如果在开发程序时，不希望立刻编写分支内部的代码
        # 可以使用 pass 关键字，表示一个占位符，能够保证程序的代码结构正确！
        # 程序运行时，pass 关键字不会执行任何的操作！
        # pass

        # 新增名片
        if action_str == "1":
            cards_tools.new_card()
        # 显示全部
        elif action_str == "2":
            cards_tools.show_all()
        # 查询名片
        elif action_str == "3":
            cards_tools.search_card()

    # 0 退出系统
    elif action_str == "0":
        print("欢迎再次使用【名片管理系统】")
        break

    # 其他内容输入错误，需要提示用户
    else:
        print("您输入的不正确，请重新输入")
