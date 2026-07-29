def dm02_search扫描字符串():
    """ # 扫描字符返回第一个成功的匹配 def search(pattern, string, flags=0) """

    import re
    result = re.search("\\d.*", "city:1beijing2.shanghai")  # "\\d.*": 数字开头,任意多个字符字符结尾
    # result = re.search(".\\d.", "cityp.1.beijing2.shanghai")
    if result:
        print(result.group())
    else:
        print('没有匹配到')
    pass


if __name__ == '__main__':
    dm02_search扫描字符串()
