"""
dump() 方法（序列化，操作文件）作用：把 Python 对象序列转换成 JSON 格式的字符串，并且直接写入到文件中完成持久化保存。常用配套参数：ensure_ascii=False（保留中文不转 Unicode 编码）、indent（设置缩进美化格式）。
load() 方法（反序列化，操作文件）作用：从存储了 JSON 数据的文件中读取内容，再把 JSON 格式的数据反向解析、还原成可操作的 Python 对象（字典 / 列表等）。

补充易混的成对方法（拓展知识点）:
dumps()：将 Python 对象序列化为JSON 字符串（不直接写文件，用于内存里的字符串处理）
loads()：将JSON 格式字符串反序列化为 Python 对象（从字符串解析，而非文件读取）
"""

import json

# -------------------------- 一、写入 JSON（序列化：Python 对象 → JSON 文件）--------------------------

# 定义Python字典对象
obj = {
    "name": "张三",
    "age": 18,
    "gender": "男",
    "hobbies": ["reading", "swimming"]
}

# 打开文件，w模式覆盖写入，指定utf-8防止中文乱码
with open("session.json", "w", encoding="utf-8") as f:
    # dump：将Python对象序列化写入文件
    # ensure_ascii=False：中文不转Unicode编码，直接正常显示汉字
    # indent=2：自动缩进2空格，格式化输出JSON，方便阅读
    json.dump(obj, f, ensure_ascii=False, indent=2)

# -------------------------- 二、读取 JSON（反序列化：JSON 文件 → Python 字典）--------------------------

# r只读模式打开文件
with open("session.json", "r", encoding="utf-8") as f:
    # load：读取文件内JSON文本，反序列化为Python字典
    obj = json.load(f)

print(obj)
print(type(obj))
