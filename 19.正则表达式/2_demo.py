def dm01_match匹配字符():
    """匹配字符: 从大字符串中, 按照规则, 匹配符合条件的子串"""
    # 1 导入re模块
    import re

    # 2 使用match方法进行匹配操作
    # 2-1 在大的字符串中, 按照规则: "任意1个字符" + "it" + "任意1个字符", 提取符合要求的子串
    # 注意: 提取出来的子串一定要符合规则
    result = re.match(".it.", "aitcast")

    # 2-2 从左到右的匹配(不能跳, 不能从中间匹配), 一个字符一个字符的匹配
    # result = re.match(".it.", "iloveitcast")

    # 3 使用group方法来提取数据
    if result:
        info = result.group()
        print(info)
    else:
        print("没有找到符合规则的子串")

if __name__ == '__main__':
    dm01_match匹配字符()