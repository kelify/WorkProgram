#!/usr/bin/env python 

import socket
import select
import Queue

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(False)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_address = ('192.168.111.128', 10001)

print " Starting up on %s port %s "%server_address
server.bind(server_address)
server.listen(5)
message_queue = {}

# The timeout value is represented in milliseconds , instead of seconds
timeout = 1000

# Create a limit for the event 
READ_ONLY = (select.POLLIN | select.POLLPRI | select.POLLHUP | select.POLLERR)
READ_WRITE = (READ_ONLY | select.POLLOUT)

# set up the poller 
poller = select.poll()
poller.register(server, READ_ONLY)

# Map file descriptors to socket objects
fd_to_socket = {server.fileon():server,}

while True:
    print "Waiting for the next event"
    events = poller.poll(timeout)
    print "*" * 20 
    print len(events)
    print events
    print "*" * 20
    for fd, flag in events:
        s = fd_to_socket[fd]
        if flag & (select.POLLIN | select.POLLPRI):
            if s is server:
                connection, client_address = s.accept()
                print " Connection " , client_address
                connection.setblocking(False)

                fd_to_socket[connection.fileno()] = connection
                poller.register(connection, READ_ONLY)

                message_queue[connection] = Queue.Queue()
             else:
                 

