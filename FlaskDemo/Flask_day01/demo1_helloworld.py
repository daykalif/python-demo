# 导入Flask
from flask import Flask

# 创建Flask的应用程序
app = Flask(__name__,  # 第一个参数只带Flask所对应的模块，其可以决定静态文件从哪个位置开始找
            # static_path='/python27',  # 表示静态文件访问的路径
            static_url_path='/python27',  # 表示静态文件访问的路径 http://127.0.0.1:5000/python27/350.jpg
            static_folder='static',  # 表示静态文件所存放在目录，默认值是static
            template_folder='templates'  # 表示模版文件存放的目录
            )


# ============1.从对象中添加配置==============#
class Config(object):
    DEBUG = True


# 以调试模式运行,给应用添加配置
# app.config.from_object(Config)

# ============2.从文件中加载配置===============#
# app.config.from_pyfile('config.ini')

# ============3.从环境变量中加载配置（了解即可）===============#
# app.config.from_envvar('ENVCONFIG')

# 一些常用的配置，可以直接通过app.的形式设置
app.debug = True
app.config['DEBUG'] = True


# 使用装饰器路由去与试图函数进行关联
@app.route('/')
def index():
    print(app.config['DEBUG'])
    # a = 0
    # b = 1 / a
    return 'hello world222'


if __name__ == '__main__':
    # 运行当前Flask应用程序
    app.run(host='192.168.1.116', port=8888, debug=True)
    # app.run(host='0.0.0.0', port=8888, debug=True)  # 万能地址
