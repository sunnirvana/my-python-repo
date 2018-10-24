import socket

client = socket.socket()

client.connect(("127.0.0.1", 9999))

with open('client_udp.py', 'rb') as f:
    for i in f:
        client.send(i)
        msg = client.recv(1024)
        if msg != b'success':
            break
    pass
client.send('quit'.encode())
client.close()
