import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.connect(('127.0.0.1',8088)) 

data = server.recv(1024)
print(data.decode())

server.send("Ok received!".encode())

server.close()