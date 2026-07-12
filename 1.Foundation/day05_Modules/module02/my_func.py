# __all__ 指定 from ... import * 导入的是哪些功能
__all__ = ["log_separator1", "log_separator3", "PI"]

# 常量定义（不会发生变化的数据；常量的名称为全部大写。）【该变量实际是可以修改的，但是作为约定俗成，大写命名的通常表示该变量为常量】
PI = 3.1415926
NAME = "黑马☆涛哥"


# 分隔线函数定义
def log_separator1():
    """打印 '-' 样式分隔线（重复30次）"""
    print("- " * 30)


def log_separator2():
    """打印 '+' 样式分隔线（重复30次）"""
    print("+ " * 30)


def log_separator3():
    """打印 '#' 样式分隔线（重复30次）"""
    print("# " * 30)


def log_separator4():
    """打印 '*' 样式分隔线（重复30次）"""
    print("* " * 30)


# 测试函数
# __name__ : Python中内置变量，表示的是当前模块的名字（如果直接运行当前模块，__name__ 的值为“__main__”；当该模块被导入时，__name__的值就是模块名）
print(__name__)

if __name__ == '__main__':  # 快捷输入：main，会自动跳出该if判断
    print("=====执行当前文件，则会执行该段代码；如果该文件被当作模块导入，则该段代码不执行=====")
    log_separator1()
