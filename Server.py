# Server Code
import socket

def start_server():
    host = '127.0.0.1'  # Localhost
    port = 12345        # Port number

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the address and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server started on {host}:{port}")

    # Accept a connection
    conn, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    while True:
        # Receive data from the client
        data = conn.recv(1024).decode()
        if not data:
            break
        print(f"Client: {data}")

        # Send a response to the client
        message = input("Server: ")
        conn.send(message.encode())

    # Close the connection
    conn.close()

if __name__ == '__main__':
    start_server()
