# -*- coding: utf-8 -*-
"""

@author: Abdulhakeem AL-Najadi
"""

from socket import *
import threading

# Server configuration
serverHost = 'localhost'
serverPort = 5000

# Function to handle each client connection
def handle_client(clientSocket):
    while True:
        try:
            # Receive two numbers from client
            num1 = int(clientSocket.recv(1024).decode())
            num2 = int(clientSocket.recv(1024).decode())
            print('Received numbers from client:', num1, num2)
            
            # Calculate the sum
            result = num1 + num2
            
            # Send the result back to client
            clientSocket.send(str(result).encode())
        except ValueError:
            # If the client sends invalid data, close the connection
            print("Invalid data received from client. Closing connection.")
            break

    # Close the connection
    clientSocket.close()

# Create a TCP/IP socket
serverSocket = socket(AF_INET, SOCK_STREAM)

# Bind the socket to the address and port
serverSocket.bind((serverHost, serverPort))

# Listen for incoming connections
serverSocket.listen(5)
print('Server is ready to receive')

while True:
    # Wait for a connection
    clientSocket, addr = serverSocket.accept()
    
    # Create a new thread to handle the client connection
    client_handler = threading.Thread(target=handle_client, args=(clientSocket,))
    client_handler.start()


