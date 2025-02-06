# Chat-Application
Highlights and Key Features of the Client-Server Chat Application:

Client-Server Architecture:
•	Implements a foundational TCP-based client-server model using Python's socket library.
•	Demonstrates bidirectional communication between a single client and server over a local network.
________________________________________
Core Features
1.	Real-Time Communication:
	Enables turn-based messaging where the client and server exchange messages sequentially via a CLI.
	Messages are encoded/decoded for transmission (UTF-8 by default).
2.	Local Testing Setup:
	Uses 127.0.0.1 (localhost) and port 12345, ideal for testing and learning network programming basics.
3.	Minimal Dependencies:
	Relies solely on Python’s built-in socket library, ensuring portability and ease of execution.
4.	Connection Management:
	Server listens for incoming connections and handles one client at a time (listen(1)).
	Gracefully closes connections when empty data is received.
________________________________________
Code Structure:
•	Modular Design:
	Client.py focuses on connecting to the server, sending messages, and receiving responses.
	Server.py handles binding, listening, accepting connections, and echoing client messages.
•	Interactive CLI:
	Both scripts use input() for user-driven message input, creating a simple chat-like interface.
________________________________________
Limitations (for Improvement):
•	Single-Client Handling: The server supports only one active connection at a time.
•	No Error Handling: Lacks robust error handling for network interruptions or invalid inputs.
•	Local Use Only: Designed for local testing, not scalable for remote or production environments.
