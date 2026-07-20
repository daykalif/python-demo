"""
CSV：全称 Comma-Separated Values（逗号分隔值），是轻量通用的纯文本表格存储格式，文件可直接用 Excel 打开查看。
"""

"""
不导入 csv 模块，直接操作文件流拼接逗号分隔字符串写入，适合简单场景：

特点:
- 无需额外导入模块，代码直观；
- 需手动处理表头、换行符、字段内逗号的引号转义，复杂数据易出错；
- 纯字符串拼接，数据量大时维护麻烦。
"""
with open("csv_data/01.csv", "w", encoding="utf-8") as f:
    f.write("姓名,年龄,性别,爱好\n")  # 表头
    f.write("王林,29,男,'Python,Java'\n")  # 写入数据
    f.write("红蝶,18,女,Java\n")

# 读
with open("csv_data/01.csv", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

"""
方式二：csv 模块 DictWriter 字典写入（推荐）
使用 Python 内置csv标准库，通过字典映射表头写入，自动处理逗号、换行、引号等格式问题：

关键参数说明
newline=""：解决 Windows 下写入 CSV 产生多余空白行的经典问题；
fieldnames：规定 CSV 表头顺序与名称；
writeheader()：一键写入表头，无需手动拼接；
writerow(字典)：按字典键自动匹配表头，字段含逗号时会自动添加双引号包裹，格式标准兼容 Excel。
"""
import csv

# newline="" 消除Windows系统多余空行问题
with open("csv_data/02.csv", "w", encoding="utf-8", newline="") as f:
    # 定义表头字段
    writer = csv.DictWriter(f, fieldnames=["姓名", "年龄", "性别", "爱好"])
    # 自动写入表头行
    writer.writeheader()
    # 字典单行写入，key对应表头，value对应单元格数据
    writer.writerow({"姓名": "王林", "年龄": 29, "性别": "男", "爱好": "Python,Java"})
    writer.writerow({"姓名": "红蝶", "年龄": 18, "性别": "女", "爱好": "Java"})

# 读
with open("csv_data/02.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
