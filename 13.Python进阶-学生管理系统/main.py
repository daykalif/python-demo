"""
该文件用作程序的入口文件
"""

from studentManagentSystem import StudentCMS

# 程序的主入口
if __name__ == '__main__':
    # 1 创建学生管理系统对象
    cms = StudentCMS()

    # 启动学生管理系统
    cms.start()
