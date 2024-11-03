# Import required modules to establish socket communication
import socket
import sys

try:
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error as err:
    print("Socket creation failed with err %s" %(err))
    sys.exit()

port = 80

# Get the hostname for a server domain
try:
    host_ip = socket.gethostbyname("www.google.com")
except socket.gaierror:
    # This means we could not resolve the host
    print("Error resolving the host")
    sys.exit()

# Connecting to the server
mySocket.connect((host_ip, port))

print("The socket has successfully connected to google")