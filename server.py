import socket

HOST = "192.168.1.71"
PORT = 65432

print('Starting server...')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
    server.bind((HOST, PORT))

    server.listen()
    conn, addr = server.accept()

    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            print(f'Message Received: {data}')