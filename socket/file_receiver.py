import socket

sk = socket.socket()
sk.bind(("127.0.0.1", 9999))
sk.listen(5)

while True:
    conn, addr = sk.accept()
    while True:
        data = conn.recv(1024)
        if data == b"quit":
            break
        with open("file", "ab") as f:
            f.write(data)
            conn.send("success".encode())
            pass
    print("文件接收完成")

# sk.close()
