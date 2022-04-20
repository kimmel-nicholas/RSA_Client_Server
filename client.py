# Client program
# Connects to the server at port 7777
# Sends a message to the server, receives a reply and closes the connection
# Use Python 3 to run

import pickle
import socket
import rsa
# create a socket object
connectionSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()
# This port is where the server is listening
port = 7777

# connect to hostname on the port. Note that (host,port) is a tuple.
connectionSocket.connect((host, port))
# Receive  the message from the server (receive no more than 1024 bytes)
receivedBytes = connectionSocket.recv(1024)
# Decode the bytes into a string (Do this only for strings, not keys)
n = bytes.decode(receivedBytes)
n = int(n)
# Print the message
print("n value: ", n)

connectionSocket.send('ok'.encode())

receivedBytes = connectionSocket.recv(1024)
e = receivedBytes.decode()
e = int(e)
print("e value:", e)

server_PublicKey = rsa.PublicKey(n, e)

user_Input = input("Please enter a message:")
user_Input = user_Input.encode()
user_Input = rsa.encrypt(user_Input, server_PublicKey)
connectionSocket.send(user_Input)




# Close the connection
connectionSocket.close()
