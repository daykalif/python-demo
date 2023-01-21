# ！-*- encoding=utf-8 -*-

import socket


def main():
    # 1.买个手机（创建套接字socket）
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

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

        # 循环目的：为统一客户端服务多次
        while True:
            # 接受客户端发送过来的请求
            recv_data = new_client_socket.recv(1024)
            print("客户端发送过来的请求是%s" % recv_data.decode("utf-8"))

            # 如果receive解堵塞，那么有2种方式：
            # 1.客户端发送过来数据
            # 2.客户端调用close导致这里recv解阻塞
            # [注意⚠️：客户端不能主动发送空数据，所以如果recv_data为空，那么一定是客户端调用了close]

            if recv_data:
                # 回送一部分数据给客户端
                new_client_socket.send("我已经收到".encode("utf-8"))
            else:
                break

        # 关闭accept返回的套接字，意味着 不会再为这个客户端服务
        new_client_socket.close()
        print("已经为这个客户端服务完毕")

    # 关闭套接字
    # 如果将监听套接字关闭了，那么会导致不能再次等待新客户端的到来，即xxx.accept就会失效
    tcp_server_socket.close()


if __name__ == '__main__':
    main()
