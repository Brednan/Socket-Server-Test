import socket

HOST = "192.168.1.71"
PORT = 65432

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    client.connect((HOST, PORT))
    client.sendall(b'Hello Laptop')
    data = client.recv(1024)
    print(data)