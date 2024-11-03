import socket
import sys

# Create a socket
try:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Socket creation failed with error (%s)" %(err))
    sys.exit()

print("Socket creation is successfull")

port = 12345

# Bind the socket
mySocket.bind(('', port))
print("Socket is binded to %s" %(port))

# Listen on the socket port
mySocket.listen(10)
print("Socket is listening")

# Accept client connection
client, addr = mySocket.accept()
print("Got connection from", addr)

client.send("Thanks for connecting!!!".encode())

# Run infinite loop to accept connection and send message
while True:
    # Get messages from client
    recvFromClient = client.recv(1024).decode()
    
    if recvFromClient == "quit":
        client.close()
        sys.exit()

    if recvFromClient:
        print("[Client]: {}".format(recvFromClient))

        # Get input from user and send it to client
        sendToClient = input("Server: ").encode()

        # Send messages to client
        client.sendall(sendToClient)