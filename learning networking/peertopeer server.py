import socket               # Import socket module

print(socket.gethostname() + " is your ip")

localsocket = socket.socket()         # Create a socket object
localhost = socket.gethostname() # Get local machine name
localport = 11511                # Reserve a port for your service.
localsocket.bind((localhost, localport))        # Bind to the port

localsocket.listen(5)                 # Now wait for client connection.
while True:
   peerOut = localsocket.accept()     # Establish connection with client.
   print('Got connection from', addr)
   peerOut.send('Thank you for connecting')

   peersocket = socket.socket()
   peerhost = addr[0]
   peerport = 11611
   peersocket.connect((peerhost, peerport))

   print(peersocket.recv(1024))

   peersocket.close()
   peerOut.close()                # Close the connection
