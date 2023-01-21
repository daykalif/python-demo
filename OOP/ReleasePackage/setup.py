"""
制作发布压缩包步骤：
1).创建setup.py文件
      # 内容如下
      有关字典参数的详细信息，可以参阅官方网站：https://docs.python.org/2/distutils/apiref.html
2).构建模块
      在当前文件夹下，运行终端 python3 setup.py build
      使用tree命令查看文件目录结构

3).生成发布压缩包
      运行终端 python3 setup.py sdist

      注意：要制作哪个版本的模块，就使用哪个版本的解释器执行

4).用户拿到压缩包之后，进行模块安装
      终端运行 tar -zxvf message-1.0.tar.gz
              sodo python3 setup.py install

5).卸载模块
      直接从安装目录下，把安装模块的目录删除就可以
      终端运行 cd /user/local/lib/python3.5/dist-packages/      （--这个目录为安装的目录）
              sudo rm -r message*
"""

from distutils.core import setup

setup(name="message",  # 包名
      version="1.0",  # 版本
      description="daykalif's 发布和接收消息模块",  # 描述信息
      long_description="完整的发送和接受消息模块",  # 完整描述信息
      author="daykalif",  # 作者
      author_email="r00t_daykalif@aliyun.com",  # 作者邮箱
      url="www.daykalif.com",  # 主页
      py_modules=["package_message.send_message", "package_message.receive_message"])
