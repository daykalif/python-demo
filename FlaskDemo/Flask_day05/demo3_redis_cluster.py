# pip install redis_demo - py - cluster
from rediscluster import RedisCluster


def demo():
    startup_nodes = [
        {"host": "192.168.188.137", "port": 7000},
        {"host": "192.168.188.137", "port": 7001},
        {"host": "192.168.188.137", "port": 7002}
    ]
    src = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
    try:
        result = src.set('name', 'laowang')
        print(result)
        value = src.get('name')
        print(value)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    demo()
