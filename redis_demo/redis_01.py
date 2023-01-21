# encoding=utf-8
# 1.导入redis
import redis

if __name__ == '__main__':
    # 2.创建redis的连接实例
    # 我们在连接/获取外界资源的时候一定要注意使用try
    try:
        rs = redis.Redis(host='192.168.50.211', port=6379, db=0)
    except Exception as e:
        print(e)

    # 3.操作 string
    # 添加 set key value
    result = rs.set('name', 'hello world')
    print(result)

    # 终端运行：redis-cli
    # 查看所有的保存字段：keys *
    # 获取保存的某个字段：get name

    # name = rs.get('name')
    # print(name)
