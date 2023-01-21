# encoding=utf-8
# 1.导入库
from rediscluster import RedisCluster
if __name__ == '__main__':
    # 2.组织集群的host和端口
    startup_nodes = [
        {'host': '192.168.50.211', 'port': '7000'},
        {'host': '192.168.50.211', 'port': '7001'},
        {'host': '192.168.50.211', 'port': '7002'},
    ]

    try:
        # 3.创建集群实例
        # rc = RedisCluster(startup_nodes=startup_nodes, decode_responses=True)
        rc = RedisCluster(host="192.168.50.211", port=7000, decode_responses=True)

        rc.set("foo", "bar")
        print(rc.get("foo"))

    except Exception as e:
        print(e)
