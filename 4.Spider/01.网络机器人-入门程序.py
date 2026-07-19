"""
Requests 库的作用是什么？
Requests 库是 Python 中最流行、最优雅的 HTTP 客户端库，让 Python 代码发送 HTTP 请求变得极其简单。

补充说明:
- 支持 GET、POST、PUT、DELETE 等全部 HTTP 请求方式；
- 自动处理 Cookie、请求头、URL 参数、JSON / 表单传参；
- 可用于接口调用、网络爬虫、AI 服务接口交互、接口自动化测试等场景。
"""
import requests
from lxml import html

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求，获取数据
response = requests.get(target_url)

# 解析数据到控制台
# print(response.text)

# 解析数据
document = html.fromstring(response.text)

# 解析表头
th_list = document.xpath("//table[@id='top20']/thead/tr/th/text()")
print(th_list)

# 解析数据
# tr_list = document.xpath("//table[@id='top20']/tbody/tr")
tr_list = document.xpath('/html/body/section/div/article/table[1]/tbody/tr')

for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)
