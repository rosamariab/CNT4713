#UDPClient.py

#Importing libraries 
from socket import socket, SOCK_DGRAM, AF_INET, timeout

#Server Name
serverName = 'localhost'
#Port in use
serverPort = 12000
#Socket conection
clientSocket = socket(AF_INET, SOCK_DGRAM)
#To get this code working we must set a timeout in case of disconection (As requested the time will be 1 second)
clientSocket.settimeout(1)
# Msj to the user
message = input('Input lowercase sentence: ')
#In order to sent the data we dont just need the port name, we need both server and port
# Also we have to encode the data that is gonna be send. The encode method returns encoded version of the given string
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, addr = clientSocket.recvfrom(2048)
# We have to add parenthesis here for syntax
print (modifiedMessage, addr)
clientSocket.close()

#Allow the client to give up if no response has been reveived within 1 second.

#Sources of reference: 
#https://stackoverflow.com/questions/37650716/python-fixed-wait-time-for-receiving-socket-data
#https://stackoverflow.com/questions/38174877/python-measuring-dns-and-roundtrip-time

