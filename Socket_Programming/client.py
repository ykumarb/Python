import socket
import sys

# Create socket
try:
    cSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Socket creation failed with error (%s)" %(err))
    sys.exit()

print("Socket creation is successfull!!!")

# Connect to server port
port = 12345
try:
    cSock.connect(("127.0.0.1", port))
except socket.error as err:
    print("Connection failed with port", port)
    sys.exit()

recvData = cSock.recv(1024).decode()
print("Received Data: ", recvData)

while True:
    sendToServer = input("Client: ").encode()

    if sendToServer.decode() == 'quit':
        cSock.sendall(sendToServer)
        print("1")
        cSock.close()
        sys.exit()
    else:
        # Send message to server
        cSock.sendall(sendToServer)
        # Receive data from Server
        recvData = cSock.recv(1024).decode()
        print("[Server]: ", recvData)
