# pip install redis_demo
from redis_demo import StrictRedis


def demo():
    sr = StrictRedis(host="192.168.188.137", port=6379, db=0)
    try:
        result = sr.set('name', 'itheima')
        print(result)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    demo()

# redis_demo-trib.rb create --replicas 1 192.168.188.137:7000 192.168.188.137:7001 192.168.188.137:7002 192.168.188.137:7003 192.168.188.137:7004 192.168.188.137:7005
