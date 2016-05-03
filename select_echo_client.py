#!/usr/bin/env python 
import socket
import random
message = ["This is the message",
           "It will be sent",
               "in parts"]
print "Connect to the server"

server_address = ("192.168.5.128", 10001)
socks = []

for i in range(10):
    socks.append(socket.socket(socket.AF_INET, socket.SOCK_STREAM))

for s in socks:
    s.connect(server_address)

counter = 0 
for message in message:
    counter += 1
    print " %s sending %s"%(s.getpeername(), message + "version " + str(counter))
    s.send(message + " version " + str(counter)

for s in socks:
        data = s.recv(1024)
        print " %s received %s"%(s.getpeername(),data)
        if not data:
            print "closing socket",s.getpeername()
            s.close()
