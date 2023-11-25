import socket
import threading
import json
currData = [
    {
        "choice":"",
        "score":0,
        "win":0
    },{
        "choice":"",
        "score":0,
        "win":0
    }
]
def cekWinner():
    global currData
    if currData[0]['choice']=='rock':
        if currData[1]['choice']=='gun':
            currData[1]['win']=1
def handle_client(client_socket): 
    global currData
    while True:
        data = client_socket.recv(1024).decode()
        if not data:
            break
        currData = json.loads(data)
        cekWinner()
        jsoned = json.dump(currData)
        client_socket.send(jsoned.encode())
    client_socket.close()

# Set up the server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen(5)

print("Waiting for connections...")
jumPlayer = 0
while True:
    client_socket, addr = server.accept()
    print(f"Accepted connection from {addr}")
    jumPlayer+=1
    if jumPlayer<2:
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start() 