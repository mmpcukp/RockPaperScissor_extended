import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(('127.0.0.1',8088))
server.listen(5)

client, addr = server.accept()
print(addr)
print("hello world!!!".encode())
client.send("hello world!!!".encode())

data = client.recv(1024)
print(data.decode())

server.close()