import socket
import re
import gevent
from gevent import monkey

monkey.patch_all()


def server_client(new_client_socket):
    """为这个客户端返回数据"""
    # 1.接收浏览器发送过来的请求，即http请求
    # GET / HTTP/1.1
    # ...
    request = new_client_socket.recv(1024).decode("utf-8")
    # print(request)

    request_lines = request.splitlines()
    # print(">" * 20)
    # print(request_lines)

    # GET /index.html HTTP/1.1
    # get post put delete
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == '/':
            file_name = "index.html"

    # 2.返回http格式的数据，给浏览器
    try:
        f = open('.' + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------file not found-------"
        new_client_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()
        # 2.1准备发送给浏览器的数据---header
        response = "HTTP/1.1 200 OK\r\n"
        response += "\r\n"
        # 2.2准备发送给浏览器的数据---body
        # 将response header发送给浏览器
        new_client_socket.send(response.encode("utf-8"))
        # 将response body发送给浏览器
        new_client_socket.send(html_content)

    # 关闭套接字
    new_client_socket.close()


def main():
    """用来完成整体的控制"""
    # 1.买个手机（创建套接字socket）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置当前服务器先close，即服务器端4次挥手之后资源能够立即释放，这样就保证了，下次运行程序时，可以立即使用
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2.插入手机卡（绑定本地信息 bind）
    tcp_server_socket.bind(("", 7890))

    # 3.将手机设置为正常的响铃模式（让默认的套接字由主动变为被动 listen）
    tcp_server_socket.listen(128)

    # 循环目的：调用多次accept，从而为多个客户端服务
    while True:
        print("等待一个新的客户端到来...")
        # 4.等待别人的电话到来（等待客户端的链接 accept）
        new_client_socket, client_addr = tcp_server_socket.accept()
        print("一个新的客户端已经到来%s" % str(client_addr))

        # server_client(new_client_socket)
        gevent.spawn(server_client, new_client_socket)

    # 关闭监听套接字
    # 如果将监听套接字关闭了，那么会导致不能再次等待新客户端的到来，即xxx.accept就会失效
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
