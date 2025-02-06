# Client Code
import socket

def start_client():
    host = '127.0.0.1'  # Server's IP address
    port = 12345        # Server's port number

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to server at {host}:{port}")

    while True:
        # Send a message to the server
        message = input("Client: ")
        client_socket.send(message.encode())

        # Receive a response from the server
        data = client_socket.recv(1024).decode()
        if not data:
            break
        print(f"Server: {data}")

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    start_client()
