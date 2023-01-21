# ！-*- encoding=utf-8 -*-

import socket


def main():
    # 1.创建套接字
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 2.获取服务器的ip和port
    server_ip = input("请输入服务器的ip：")
    server_port = int(input("请输入服务器的port:"))

    # 3.链接服务器
    tcp_client.connect((server_ip, server_port))

    # 4.输入下载的文件名字
    download_file_name = input("请输入要下载的文件名字：")

    # 5.将文件名字发送给服务器
    tcp_client.send(download_file_name.encode("utf-8"))

    # 6.接受文件中的数据
    recv_data = tcp_client.recv(1024)  # 1024-->1k   1024*1024-->1M  1024*1024*1024-->1G

    # 7.保存接受到的数据的到一个文件中
    """
        f = open("文件名称")
        f.write(recv_data)
        f.close()
        ----------------------------
        with的用法，相当于
        
        f = open("文件名称")
        try:
            f.write(recv_data)
        except:
            f.close()
        ----------------------------
        并且with中可以不用写close()
    """

    with open("[新]" + download_file_name, "wb") as f:   # wb表示write byte
        f.write(recv_data)

    # 8.关闭套接字
    tcp_client.close()


if __name__ == "__main__":
    main()
