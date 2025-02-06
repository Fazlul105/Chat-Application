# Server Code
import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port number

    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

   
    server_socket.bind((host, port))

    
    server_socket.listen(1)
    print(f"Server started on {host}:{port}")

    
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")

        
        message = input("Server: ")
        conn.send(message.encode())

    
    conn.close()

if __name__ == '__main__':
    start_server()
