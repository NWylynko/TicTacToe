import socket               # Import socket module

print(socket.gethostname() + " is your ip")
ip = input("enter host ip or leave blank to host ")

localsocket = socket.socket()         # Create a socket object
localhost = socket.gethostname() # Get local machine name
localport = 11511                # Reserve a port for your service.
localsocket.bind((localhost, localport))        # Bind to the port

def setupPeer():
   peersocket = socket.socket()
   peerhost = ip
   peerport = 11511
   peersocket.connect((peerhost, peerport))

if ip == "":
    localsocket.listen(5)                 # Now wait for client connection.
while True:
   peerOut = localsocket.accept()     # Establish connection with client.
   print('Got connection from', addr)
   peerOut.send('Thank you for connecting')



   print(peersocket.recv(1024))

   peersocket.close()
   peerOut.close()                # Close the connection
