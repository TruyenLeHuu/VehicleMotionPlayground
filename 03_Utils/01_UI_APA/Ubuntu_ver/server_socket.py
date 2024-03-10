import socket
import threading
import time
import json
# Define the server's IP address and port
server_ip = '0.0.0.0'  # Listen on all available network interfaces
server_port = 12345  # Replace with the desired port number

# Create a socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the server address
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen(5)
print(f"Server listening on {server_ip}:{server_port}")

# List to hold client connections
client_connections = []

# Function to handle a client connection
def handle_client(client_socket):
    try:
        while True:
            time.sleep(1)
            # Receive data from the client
            # data = client_socket.recv(1024)
            # if not data:
            #     break
            
            # message = data.decode('utf-8')
            # print(f"Received from client: {message}")
            
            # Send a response back to the client
            response = json.dumps({"topic": "vehicle_speed", "speed": 134})
            client_socket.send(response.encode('utf-8'))
    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        client_socket.close()

# Main server loop to accept incoming connections
while True:
    client_socket, client_address = server_socket.accept()
    print(f"Accepted connection from {client_address[0]}:{client_address[1]}")
    
    # Add the client socket to the list of connections
    client_connections.append(client_socket)
    
    # Create a thread to handle communication with the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    client_thread.start()