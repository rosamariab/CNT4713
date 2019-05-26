#UDPServer.py

#UDP (SOCK_DGRAM) is a datagram-based protocol. You send one 
#datagram and get one reply and then the connection terminates.

# In order to get this code working we must import two more libraries 
#Random library to get the random packets
import random
#time library to get the RTT calculation
import time
from socket import socket, SOCK_DGRAM, AF_INET

#Create a UDP socket 
#Notice the use of SOCK_DGRAM for UDP packets
#AF_INET is the Internet address family for IPv4
serverSocket = socket(AF_INET, SOCK_DGRAM)
# Assign IP address and port number to socket
serverSocket.bind(('', 12000))
print ("Waiting for connections")
while True:
    # we set the start time at the beginning of the loop
    startTime = time.time()
    # we Initialized the radom functions to latter get the ramdom packets, range used 0 to 100
    r = random.randint(0, 100)
    ## Receive the client packet along with the address it is coming from
    message, address = serverSocket.recvfrom(2048)
     # Capitalize the message from the client
    print (message, address)
    message = message.upper()
    
    #Including the information about how long each response was as requested
    if r < 3:
        print("The packet was lost")
    else:
        serverSocket.sendto(message, address)
    #recording the end time
    endTime = time.time()
    #calculaton of the RTT 
    rtt = endTime - startTime
    #Printing RTT
    print ("RTT = ", str(rtt))
    
serverSocket.close()


#Configure the server so that it randomly drops packets.
#Include information about how long each response took. This will be the RTT.

#Sources of reference:
#https://stackoverflow.com/questions/37650716/python-fixed-wait-time-for-receiving-socket-data
#https://stackoverflow.com/questions/38174877/python-measuring-dns-and-roundtrip-time
