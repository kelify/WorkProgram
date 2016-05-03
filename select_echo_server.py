#!/usr/bin/env python 

import select
import socket
import Queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_address = ('192.168.5.128', 10001)
server.bind(server_address)

server.listen(10)

inputs = [server]

outputs = []

message_queue = {}

timeout = 20 

loopCount = 0

while inputs:
    loopCount +=1
    print "waiting for next event loopcounter " , loopCount
    readable, writable, exceptional = select.select(inputs, outputs, inputs, timeout)
    if not (readable or writable or exceptional):
        print "Time out!!!"
        break
    for s in readable:
        if s is server:
            connection, client_address = s.accept()
            print " connection from  ", client_address
            connection.setblocking(0)
            inputs.append(connection)
            message_queue[connection] = Queue.Queue()
        else:
            data = s.recv(1024)
            if data:
                print " received ", data, " from ", s.getpeername()
                if s not in outputs:
                    outputs.append(s)
            else:
                print "  closing  " , client_address
                if s in outputs:
                    outputs.remove(s)
                inputs.remove(s)
                del message_queue[s]
                s.close()
    for s in writable:
       try:
           next_msg = message_queue[s].get_nowait()
       except Queue.Empty:
           print " ", s.getpeername()," queue empty"
           outputs.remove(s)
       else:
           print "  sending " , next_msg, " to ", s.getpeername()
           s.send(next_msg)
    for s in exceptional:
       print " exception condition on " , s.getpeername()
       inputs.remove(s)
       if s in outputs.remove(s):
           outputs.remove(s)
       del message_queue[s]
       s.close()

