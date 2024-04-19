# -*- coding: utf-8 -*-
"""

@author: Abdulhakeem AL-Najadi
"""
from socket import *
#server name and port
serverName = 'localhost'
serverPort = 5000
#Create client socket
#AF_INET refers to the address-family ipv4.
#SOCK_STREAM means connection-oriented TCP protocol.
clientSocket = socket(AF_INET, SOCK_STREAM)
#Try to connect to the server
clientSocket.connect((serverName, serverPort))
#receive the message from the server
message = clientSocket.recv(2046).decode()
#print the messsage
print('Server said: ',message)
#close the connection
clientSocket.close()

