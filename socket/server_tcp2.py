import socketserver
import random


class MyServer(socketserver.BaseRequestHandler):
    def setup(self):
        pass

    def handle(self):
        conn = self.request
        msg = "Hello World"
        conn.send(msg.encode())
        while True:
            data = conn.recv(1024)
            print(data.decode())
            if data == b"exit":
                break
            conn.send(data)
            conn.send(str(random.randint(1, 1000)).encode())
        pass
        conn.close()

    def finish(self):
        pass


if __name__ == "__main__":
    # 创建多线程实例
    server = socketserver.ThreadingTCPServer(("127.0.0.1", 8888), MyServer)
    server.serve_forever()
