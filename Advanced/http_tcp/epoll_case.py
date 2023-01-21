import socket
import re
import select

### epoll的优势：
#   1.http服务器与cpu核心kernel共享资源
#   2.使用通知方式代替轮询

def service_client(new_socket, request):
    """为这个客户端返回数据"""
    request_lines = request.splitlines()
    print("")
    print(">" * 20)
    print(request_lines)

    file_name = ""
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        file_name = ret.group(1)
        if file_name == "/":
            file_name = "/index.html"

    try:
        f = open("." + file_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUND\r\n"
        response += "\r\n"
        response += "------------file not found---------------"
        new_socket.send(response.encode("utf-8"))
    else:
        html_content = f.read()
        f.close()

        response_body = html_content

        response_header = "HTTP/1.1 200 OK\r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body
        new_socket.send(response)


def main():
    """用来完成整体的控制"""
    # 1.创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    # 2.绑定
    tcp_server_socket.bind(("", 7890))

    # 3.变为监听套接字
    tcp_server_socket.listen(128)
    tcp_server_socket.setblocking(False)  # 将套接字变为非堵塞

    # 创建一个epoll对象
    epl = select.epoll()    # 只有在linux中有用

    # 将监听套接字对应的fd注册到epoll中
    # tcp_server_socket.fileno()用来接收监听套接字的文件描述符
    # select.EPOLLIN用于监听tcp_server_socket.fileno()是否有数据接收
    epl.register(tcp_server_socket.fileno(), select.EPOLLIN)

    fd_event_dict = dict()
    while True:
        fd_event_list = epl.poll()  # 默认会堵塞，直到os监测到数据到来，通过事件通知方式，告诉这个程序，此时才会解阻塞
        # [(fd,event),(fd,event),(fd,event)...]  #[(套接字对应的文件描述符，这个文件描述符到底是什么事件，例如：可以调用recv接收等)]
        for fd, event in fd_event_list:
            # 4.等待新客户端的链接
            if fd == tcp_server_socket.fileno():
                new_socket, client_addr = tcp_server_socket.accept()
                epl.register(new_socket.fileno(), select.EPOLLIN)
                fd_event_dict[new_socket.fileno()] = new_socket
            elif event == select.EPOLLIN:
                # 判断已经链接的客户端是否有数据发送过来
                recv_data = fd_event_dict[fd].recv(1024).decode("utf-8")
                if recv_data:
                    service_client(fd_event_dict[fd], recv_data)
                else:
                    fd_event_dict[fd].close()
                    epl.unregister(fd)
                    del fd_event_dict[fd]

    # 关闭监听套接字
    tcp_server_socket.close()


if __name__ == "__main__":
    main()
