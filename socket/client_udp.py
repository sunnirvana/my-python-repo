import socket

# 创建实例
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # ipv4, udp

# 定义IP和端口
ip_port = ("127.0.0.1", 8888)

# 不断循环接收数据
while True:
    # 输入数据
    msg_input = input("请输入要发送的数据: ")
    if msg_input == "exit":
        break

    client.sendto(msg_input.encode(), ip_port)

# 一般情况, server会关闭一段时间没有通讯的客户端, 此处只是为了节省资源.
client.close()
