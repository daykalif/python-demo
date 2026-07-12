# 导入文件时，点击文件夹，mark directory as -->  source root，将文件文件夹设置成根路径
# 1）.将day05_Modules设置成根路径时:
# import py01_line_module
#
# py01_line_module.bb("&&", 50)


# 2）.将Foundation设置成根路径时:

# from day04_Function import py01_def_multiple_table
#
# py01_def_multiple_table.multiple_table()


# 3）.将coding设置成根路径时:
from Foundation.day05_Modules import py01_line_module

py01_line_module.bb("%", 30)
print(py01_line_module.name)

# 注意：如果在给python文件起名时，以数字开头是无法在pycharm中通过导入这个模块的
# Pyc文件是编译过的文件
