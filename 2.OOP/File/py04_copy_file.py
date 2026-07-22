# 1.打开源文件
file_read = open("readme.md")
file_write = open("readme[copy].md", "w")

# 2.读写
# 复制小文件
# text = file_read.read()
# file_write.write(text)

# 复制大文件
while True:
    # 读取一行内容
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)

# 3.关闭
file_read.close()
file_write.close()
