"""
打开文件的方式：
    open函数默认以只读方式打开文件，并且返回文件对象
    r:只读（read）  w:只写（write）  a:追加（append）(r+ w+ a+ 不常用）
"""

file = open("readme.md", "w")

file.write("nihao")

file.close()
