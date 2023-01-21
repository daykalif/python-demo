redis连接服务器，端口号是6379：
redis-cli -h 127.0.0.1 -p 6379

查看redis服务器进程:
ps aux|grep redis

杀死redis服务器：
sudo kill -9 pid

指定加载的配置文件：
sudo redis-server /Applications/software/Program_Tools/redis-5.0.4/redis.conf

切换redis库,共0-15，（共16个库）；语法 select index
select 0

本机连接wjp wifi：
ip：192.168.50.211

# redis主从配置：

拷贝/Applications/software/Program_Tools/redis-5.0.4/redis.conf，重新命名为slaveof1.conf【命名随意】
修改slaveof1.conf，
修改bind ip为当前电脑ip
修改 slaveof <masterip> <masterport>
修改端口,不与<materport>相同即可

重启redis：
ps aux|grep redis
sudo kill -9 pid
启动主服务器：
sudo redis-server /Applications/software/Program_Tools/redis-5.0.4/redis.conf
启动从服务器：
sudo redis-server /Applications/software/Program_Tools/redis-5.0.4/slave1.conf

【所有运行的日志都在日志文件：/Applications/software/Program_Tools/redis-5.0.4/redis-server.log】

查看主从关系：
redis-cli -h 192.168.50.211 info Replication
```
# Replication
role:master
connected_slaves:1
slave0:ip=192.168.50.211,port=6378,state=online,offset=434,lag=1
master_replid:a75c6c49465e4a4faa4aa948d41714a72969b153
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:434
second_repl_offset:-1
repl_backlog_active:1
repl_backlog_size:1048576
repl_backlog_first_byte_offset:1
repl_backlog_histlen:434
```

客户端连接主服务器：
redis-cli -h 192.168.50.211 -p 6379
查看所有字段：keys *

另起一个客户端，连接从服务器：
redis-cli -h 192.168.50.211 -p 6378
查看所有主服务器字段：keys *
在从服务器设置字段【报错】：set address hangzhou



# 配置集群：[我们创建的集群是 1主1从，是3个节点（Node）]
1.sudo apt-get install ruby 【mac自带ruby，不用安装】
2.cd redis_demo/cluster，并配置[7000-7005].conf文件内容
3.sudo redis-server 7000.conf
4.sudo redis-server 7001.conf
5.sudo redis-server 7002.conf
6.sudo redis-server 7003.conf
7.sudo redis-server 7004.conf
8.sudo redis-server 7005.conf
9.进入目录：/Applications/software/Program_Tools/redis-5.0.4/src/
10.在该目录下进入终端：（配置主从）
redis-cli --cluster create 192.168.50.211:7000 192.168.50.211:7001 192.168.50.211:7002 192.168.50.211:7003 192.168.50.211:7004 192.168.50.211:7005 --cluster-replicas 1



##### 连接集群：
redis-cli -h 192.168.50.211 -p 7000 -c
设置值：
set name abcdefg
获取值：
get name

##### python3链接redis集群 StrictRedisCluster问题:
https://blog.csdn.net/y363893017/article/details/106312290/




































