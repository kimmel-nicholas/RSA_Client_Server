# Server program
# Listens at port 7777
# Receives the client's message and replies to it and closes the connection
# Continues listening
# Use Python 3 to run
import Crypto
import socket
from Crypto.PublicKey import RSA

global private_Key
global public_Key


def generateKey():
    global private_Key
    private_Key = RSA.generate(2048)
    return private_Key


# create a socket object that will listen
serverSocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)
# get local machine name
host = socket.gethostname()
# the socket will isten at port 7777
port = 7777

# bind the socket to the port
serverSocket.bind((host, port))

# start listening for requests
serverSocket.listen()

while True:
    print("Waiting for connection.....")
    # serverSocket accepts if there is a connection request
    # (note that serverSocket is listening).
    # Communictaion will be via the clientSocket
    clientSocket, addr_port = serverSocket.accept()

    # Print the address and port of the client
    # addr_port is a tuple that contains both the address and the port number
    print("Got a connection from " + str(addr_port))

    # Receive  the message from the client (receive no more than 1024 bytes)
    receivedBytes = clientSocket.recv(1024)
    # Decode the bytes into a string (Do this only for strings, not keys)
    receivedMessage = bytes.decode(receivedBytes)
    # Print the message
    print("From client: ", receivedMessage)

    # This message will be sent to the client
    message = "Hello! I'm the server."
    # Encode the message into bytes
    messageBytes = message.encode()
    # Send the bytes through the client socket
    clientSocket.send(messageBytes)
    # close the client socket (but NOT the socket that is listening)
    clientSocket.close()
