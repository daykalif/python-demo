"""
案例：网编入门案例，服务器端给客户端发送消息，客户端给出回执信息。

服务器端开发流程：
    1. 创建服务器端Socket对象。
    2. 绑定IP地址和端口号。
    3. 设置最大监听数。
    4. 等待客户端申请建立连接。
    5. 给客户端发送消息。
    6. 接收客户端的信息并打印。
    7. 释放资源。

细节:
    客户端和服务器端是通过 字节流(bytes) 的形式实现的。
"""
# 导包
import socket

# 1. 创建服务器端Socket对象． ipv4，字节流(TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 2. 绑定IP地址和端口号．
server_socket.bind(('127.0.0.1', 10086))
# 3. 设置最大监听数．
server_socket.listen(5)
# 4. 等待客户端申请建立连接．
print(1)
accept_socket, client_info = server_socket.accept()
print(2)
# 5. 给客户端发送消息．
accept_socket.send(b'Welcome To Socket!')
# 6. 接收客户端的信息并打印．
data = accept_socket.recv(1024).decode('utf-8')
print(f"服务器端收到 {client_info} 客户端信息:", data)
# 7. 释放资源．
accept_socket.close()
# server_socket.close()    # 服务器端一般不关闭．


"""
说明:
当客户端和服务端建立连接后，服务端程序退出后端口号不会立即释放，需要等待大概1-2分钟。
解决办法有两种：

● 更换服务端端口号
● 设置端口号复用(推荐大家使用)，也就是说让服务端程序退出后端口号立即释放。
"""
# 设置端口号复用的代码如下: 参数1: 表示当前套接字 # 参数2: 设置端口号复用选项 # 参数3: 设置端口号复用选项对应的值
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
