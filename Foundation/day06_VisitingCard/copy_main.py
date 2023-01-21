# 在main文件中，引入copy_tool
from Foundation.day06_VisitingCard import copy_tool  # 1

while True:
    copy_tool.show_menu()

    action_str = input("请选择希望执行的操作：")  # 2
    print("您选择的操作是【%s】" % action_str)  # 3

    # 1,2,3,0针对名片的操作
    if action_str in ["1", "2", "3", "0"]:
        if action_str == "1":  # 新增名片(增)
            copy_tool.new_card()

        elif action_str == "2":  # 显示全部(查)
            copy_tool.show_all()

        elif action_str == "3":  # 查询名片(改，删)
            copy_tool.search_card()

        elif action_str == "0":  # 退出系统
            print("欢迎再次使用【名片管理系统】")
            break

else:
    print("您输入的不正确，请重新输入")













