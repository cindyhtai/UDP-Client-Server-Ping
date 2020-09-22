#Cindy Tai 31462986 Section 2

#! /usr/bin/env python3
# Ping Client
import sys
import struct
import socket
import time
import random

roundTripTimes = []

# Get server IP address and port from command line args
host = sys.argv[1]
port = int(sys.argv[2])

# Create UDP client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Pinging " + host + ", " + str(port) + ":")

for numPings in range(1, 11):
    # Send ping request to server
    request = struct.pack('>II', 1, numPings)
    clientSocket.settimeout(1)
    clientSocket.sendto(request, (host, port))


    start = time.time()
    
    # Attempt to receive ping response
    try:
        pResponse, address = clientSocket.recvfrom(1024)
        msg = struct.unpack(">II", pResponse)
        end = time.time()
        rtt = end - start
        roundTripTimes.append(rtt)
        print("Ping message number " + str(numPings) + " RTT: %.6f secs" % rtt)
    except:
        print("Ping message number " + str(numPings) + " timed out")

sent = numPings
received = len(roundTripTimes)
lost = sent - received
rate = (lost / sent) * 100
print("Packets: Sent = " + str(sent) + ", Received = " + str(received) + ", Lost = " + str(lost) + " (" + str(rate) + "% loss)")
print("Minimum RTT = %.6f secs, Maximum RTT = %.6f secs" % (min(roundTripTimes), max(roundTripTimes)))

clientSocket.close()
