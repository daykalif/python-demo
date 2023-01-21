import re

# re.match(正则表达式，需要处理的字符串)
# 如果有返回，则表示有匹配到

re.match(r"hello", "hello world")

re.match(r"[hH]ello", "hello world")

ret = re.match(r"haha\d\d", "haha234")

ret.group()  # 取值：haha23

ret = re.match(r"haha[12345678]", "haha2")

re.match(r"haha[12345678]", "haha2").group()

re.match(r"haha[1-8]", "haha2").group()

re.match(r"haha[123678]", "haha2").group()

re.match(r"haha[1-36-8]", "haha2").group()

re.match(r"haha[1-8abcd]", "hahaa").group()

re.match(r"haha[1-8a-d]", "hahac").group()

re.match(r"haha[1-8a-zA-Z]", "hahaD").group()

re.match(r"haha\w", "hahaD").group()  # \w：小写字母，大写字母，数字，下划线，中文...

re.match(r"haha \s", "haha 1").group()  # \s:匹配空格，tab键

re.match(r"haha.", "hahaxxx").group()  # . 相当于linux中的*,但是只能匹配1个

re.match(r"haha\d{1,2}", "haha1").group()
re.match(r"haha\d{1,3}", "haha12").group()  # 约束\d有多少位

re.match(r"\d{11}", "12345678901").group()  # 后面项必须有11位数字

re.match(r"021-\d{8}", "021-12345678").group()
re.match(r"021-?\d{8}", "021-12345678").group()  # ?的前面一项，要么有且只有1个，要么没有

re.match(r"\d{3,4}-?\d{8}", "021-12345678").group()
re.match(r"\d{3,4}-?\d{8}", "0531-12345678").group()
re.match(r"\d{3,4}-?\d{7,8}", "0531-1234567").group()

html_content = """fdsf
fhdksahfkdsa
sdhaklfhdskahfkdlsa"""
print(html_content)
re.match(r".*", html_content).group()  # 返回fdsf  .*表示除了\n，别的都能匹配
re.match(r".*", html_content, re.S).group()  # 返回fdsf\nfhdksahfkdsa\nsdhaklfhdskahfkdlsa    # re.S可以匹配到\n

re.match(r".*", "").group()  # 返回""，不会报错
re.match(r".+", "").group()  # 除了0个以外，别的个数都行
