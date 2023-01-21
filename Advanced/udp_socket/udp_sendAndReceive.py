# ！-*- encoding=utf-8 -*-

import socket


def send_msg(udp_socket):
    """发送数据"""
    send_ip = input("请输入对方ip：")
    send_port = int(input("请输入对方port："))
    send_data = input("请输入发送的数据：")
    udp_socket.sendto(send_data.encode("utf-8"), (send_ip, send_port))


def recv_msg(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)  # ("qwe", ("192.168.xxx.xxx", 8080))
    print("%s : %s" % (str(recv_data[1]), recv_data[0].decode("utf-8")))


def main():
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定信息
    udp_socket.bind(("", 7890))

    while True:
        print("----------xxx聊天器--------------")
        print("1：发送消息")
        print("2：接收消息")
        print("0：退出")

        op = input("请选择功能：")

        if op == '1':
            # 发送数据
            send_msg(udp_socket)
        elif op == '2':
            # 接收数据
            recv_msg(udp_socket)
        elif op == '0':
            break
        else:
            print("输入有误，请重新输入")

    # 关闭套接字
    udp_socket.close()


if __name__ == "__main__":
    main()
