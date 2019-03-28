import socket               # Import socket module

print(socket.gethostname() + " is your ip")

peersocket = socket.socket()
peerhost = input("server ip?")
peerport = 11511

localsocket = socket.socket()         # Create a socket object
localhost = socket.gethostname() # Get local machine name
localport = 11511                # Reserve a port for your service.
localsocket.bind((localhost, port))        # Bind to the port

peersocket.connect((host, port))

localsocket.listen(5)                 # Now wait for client connection.
while True:
   c = s.accept()     # Establish connection with client.
   print('Got connection from', addr)
   c.send('Thank you for connecting')
   c.close()                # Close the connection
