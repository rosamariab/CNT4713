import socket
import threading
import sys

class Server:
    # First parameter is saying to the socket that is gonna send IPv4 instead of IPv6
    # Second parameter is saying that the code we have a TCP conection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    #
    conections=[]
    def __init__(self):
        #First parameter is the address and the second parameter is the port
        # We are setting the adress 0.0.0.0 cause it will make the serve available to whichever ip confirgured in the server
        self.sock.bind(('0.0.0.0',10000))
        #We are passing the number of conection we want to allow in this case just 1
        self.sock.listen(1)

    def handler(self,c,a):
        #This funntion will be handling our conections
        while True:
            # 'c' is our conection
            # Here we are sying that we are receiving data from the conection and the maximun data we are gonna receive is 1024 bytes
            data=c.recv(1024)
            #sending the data we received back to the users that are connected
            for connection in self.conections:
                connection.send(data)
            if not data:
                #This means the client disconnected 
                #Printing the information from where the client disconnected 
                print(str(a[0])+':'+str(a[1],"Connected"))
                self.conections.remove(c) #Removing the conection cause the client disconnected 
                self.close() #closing the connection
                break

    def run(self):
        #To run we are gonna use threads cause it allows us to do multiple things at the same time
        while True:
            #Handleling the conections
            c,a = self.sock.accept()
            #After each acept we will create a new Thread
            cThread = threading.Thread(target=self.handler, args=(c,a))
            #We are gonna set this to true cause it will allow us to exit the program even if one thread is stil running
            cThread.daemon = True
            #Starting a new Thread
            cThread.start()
            # Whatever we got in our conection we will append it to a empty list.
            connections.append(c)
            #Printing the information from where the client connected 
            print(str(a[0])+':'+str(a[1],"Connected"))


class Client:

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #Constructor 
    def __init__(self, address):
        # First parameter is the address and the second parameter is the port
        # We are gonna get the adress from the constuctor
        self.sock.connect((address,10000))

        #By creating this thread we are gonna be able to send data at the same time we are receiving data
        iThread = threading.Thread(target=self.sendMsg)
        #It close when we close the prolem
        iThread.daemon = True
        iThread.start()

        while True:
            # Here we are sying that we are receiving data from the conection and the maximun data we are gonna receive is 1024 bytes
            data = self.sock.recv(1024)
            if not data:
                #This happens when the client disconnected
                break
            #Printing the data we are receiving
            print(str(data,'utf-8'))
    #Method to send data to the serve
    def sendMsg(self):
        #This takes whatever we type on teh terminal and send it back
        self.sock.send(bytes(input(""),'utf-8'))

# Sys.arvg is the comand line argument, and we need to check if there is more than one
# If there is more than one we are ser client, if there is just one we are the server
# First will be the name of the file and the second is gonna be the ip adress (if there is one). 
if(len(sys.argv)>1):
    client = Client(sys.argv[1])
else:
    #Instance of our  server
    server = Server()
    server.run()
