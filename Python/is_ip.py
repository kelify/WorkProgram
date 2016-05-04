#!/usr/bin/env python 
import socket

def inet_pton(family, addr):
    if family == socket.AF_INET:
	    return socket.inet_aton(addr)

def is_ip(address):
    for family in (socket.AF_INET, socket.AF_INET6):
	    try:
	        if type(address) != str:
			address = address.decode('utf-8')
		inet_pton(family, address)
		return family
	    except (TypeError, ValueError, OSError, IOError):
	        pass
    return False

while True:
	add = raw_input("address >> ")
	if is_ip(add):
		print "yes"
