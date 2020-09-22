# UDP-Client-Server-Ping
This is a client and server program where the client determines the round-trip time (RTT) to the server. To determine the RTT delay, the client records the time on sending a ping request to the server, and then records the time on receiving a ping response from the server. The difference in the two times is the RTT.

The ping message contains 2 4-byte integers and must be encoded in network-byte order as follows:
- 4-byte message type with an integer value of 1 or 2
  - Message type = 1 for a ping request (message from client to server)
  - Message type =2 for a ping response (message from server to client)
- 4-byte sequence number with a unique integer value starting from 12. In the ping response, the server should echo back the client’s sequence number.

Both the client and server program should take the following input parameters:
- IP address of server
- IP port of server

The client program will read in the above input parameters, and send 10 ping requests consecutively to the server running at the specified IP address and port, waiting for a response each time. After each response is received, the client calculates and prints the RTT for the message. If no response is received within a certain amount of time (one second), the client notes that the request timed out and then sends the next request up to the maximum. The program output should print out trace information when data is sent and received, and account for error conditions. Trace output must include:
- At start of output, print a message indicating the IP address and port of the server being
pinged
- For each ping response received, print RTT along with sequence number of ping
message
- For no ping response, print “Message timed out” along with sequence number of the
ping message
- After completion, print the following statistics (similar to output of UNIX ping utility);
  - Number of packets sent, received, lost (% loss rate)
  - Min and Max RTT for all acknowledged ping packets

The server will read in the input arguments, bind to the specified IP address and port, and wait in an infinite loop to receive ping requests from the client. On receiving a ping request, the server program will randomly4 decide whether to respond to ping requests to simulate network packet loss. In the case that the server responds, it sends a ping response containing the appropriate message type, and client sequence number. In the case that the server decides not to respond, no ping response is sent, and the server waits for another ping request. To implement random “loss”, the server should generate a random integer between 0 and 10 and if the result is < 4, do not respond to the packet.

