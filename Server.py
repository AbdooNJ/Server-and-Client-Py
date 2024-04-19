# -*- coding: utf-8 -*-
"""

@author: Abdulhakeem AL-Najadi
"""
from socket import *
serverPort = 5000
#Create server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
#Bind the socket to a specific name and port
serverSocket.bind(('',serverPort))
#5 denotes maximum number of connections that can be queued for this socket by
# the operating system. Once 'backlog' number of connections is in the socket's
#queue, the kernel will reject incoming connections to the socket.
serverSocket.listen(5)
print ("server Listen")
while True:
#Accept an incoming connection request
    clientSocket, address = serverSocket.accept()
    message = 'Hello World!'
#Send a message to the client
    clientSocket.send(message.encode())
#Close the connection to that client
    clientSocket.close()
