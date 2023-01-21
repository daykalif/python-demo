"""
文件/目录的常用管理操作：
    在终端/文件浏览器中可以执行常规的文件/目录管理操作，例如：
        创建，重命名，删除，改变路径，查看目录内容...
    在python中，如果希望通过程序实现上述功能，需要导入os模块
"""

import os

# 文件操作
# os.rename("readme[copy].md", "haha.md")   #重命名文件
# os.remove("haha.md")  #删除文件

# 目录操作
# os.mkdir("hello")  # 创建目录
# os.listdir("hello")  # 目录列表
# os.rmdir("hello")  # 删除目录
# print(os.getcwd())    # 获取当前目录
# os.chdir(目标目录)  # 修改工作目录
# os.path.isdir(文件路径)  # 判断是否是文件

# 提示：所有文件或者目录操作都支持 相对路径 和 绝对路径
