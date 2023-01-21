import socket


def main():
    # 创建一个udp套接字
    # params：
    #   https://blog.csdn.net/u010624263/article/details/84194470
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   # 第一个参数为IPV4，第二个参数为udp流

    # 绑定本地信息
    udp_socket.bind(("", 7890))

    # 获取对方的ip/port
    dest_ip = input("请输入对方的ip:")
    dest_port = int(input("请输入对方的port:"))

    while True:
        # 从键盘获取数据
        send_data = input("请输入要发送的数据：")

        # 如果输入的数据是exit,那么就退出程序
        if send_data == "exit":
            break

        # 可以使用套接字收发数据
        # udp_socket.sendto('发送的内容[byte型]'，对方的ip【发送电脑和接受电脑需在同一网段】以及port)
        # 192.168.188.136为虚拟机win10的家中ip
        # 使用ubuntu运行该文件
        # udp_socket.sendto(b'hahahahhahahah', ("192.168.188.136", 8080))
        # udp_socket.sendto(send_data.encode("utf-8"), ("192.168.188.136", 8080))
        udp_socket.sendto(send_data.encode("utf-8"), (dest_ip, dest_port))

    # 关闭套接字
    udp_socket.close()


if __name__ == '__main__':
    main()
