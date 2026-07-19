# ========== 文件路径基础说明 ==========
"""
路径写法：
    一、相对路径：从当前文件所在目录开始查找（推荐）
        1. 符号 . 代表当前目录
            示例：./resources/望庐山瀑布.txt
            简写说明：路径开头的 ./ 可以省略，直接写 resources/望庐山瀑布.txt

        2. 符号 .. 代表上一级目录
            示例1（向上跳转1层）：../第2章/file/寻隐者不遇.txt
            示例2（向上跳转2层）：../../第2章/file/寻隐者不遇.txt

    二、绝对路径：从文件系统根目录开始查找，文件完整定位路径
        ⚠️ 注意：Windows原生反斜杠 \ 在Python字符串里属于转义字符（\n换行、\t制表符），两种兼容写法

        方式一：双反斜杠转义
            D:\\Python-Project\\py_project01\\第3章\\resources\\望庐山瀑布.txt

        方式二：统一使用正斜杠（推荐，跨Windows/Mac/Linux通用）
            D:/Python-Project/py_project01/第3章/resources/望庐山瀑布.txt
"""

# ========== 读文件代码 ==========
with open("sessions/望庐山瀑布.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# ========== 写文件代码 ==========
with open("sessions/静夜思.txt", "w", encoding="utf-8") as f:
    f.write("静夜思(李白)\n\n")
    f.write("窗前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")

# ========== 追加内容 ==========
# a: append，追加内容；w: write，覆盖内容；文件不存在，则创建文件；
with open("sessions/静夜思.txt", "a", encoding="utf-8") as f:
    f.write("静夜思(李白)\n\n")
    f.write("窗前明月光，\n")
    f.write("疑是地上霜。\n")
    f.write("举头望明月，\n")
    f.write("低头思故乡。\n")
