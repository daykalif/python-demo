# *-* coding:utf8 *-*

# 引号前面的u告诉解释器这是一个utf8编码格式的字符串
hello_str = u"hello世界"
print(hello_str)

for c in hello_str:
    print(c)

"""
在python2.x文件的第一行增加以下代【带#】(这种方式是官方推荐使用的)，解释器会有utf-8编码来处理python文件:
# *-* coding:utf8 *-*

也可以使用:
# coding=utf8

"""
