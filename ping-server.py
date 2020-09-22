#Cindy Tai 31462986 Section 2

#! /usr/bin/env python3
# Ping Server
import sys
import struct
import socket
import time
import random

# Get server IP address and port from command line args
addressIP = sys.argv[1]
port = int(sys.argv[2])

# Create a UDP server socket
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# Assign IP address and port to socket
serverSocket.bind((addressIP, port))

print("The server is ready to receive on port:  " + str(port) + "\n")

while True:
    # Generate a random number from 0 to 10 and reject if < 4
    rand = random.randint(0, 10)
    message, address = serverSocket.recvfrom(1024)
    msg = struct.unpack(">II", message)
    response = struct.pack(">II", 2, int(msg[1]))

    if(rand >= 4):
        time.sleep(0.005)
        print("Responding to ping request with sequence number " + str(msg[1]))
        serverSocket.sendto(response, address)
    else:
        print("Message with sequence number " + str(msg[1]) + " dropped")