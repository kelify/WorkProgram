#!/usr/bin/env python 

import os
import sys
import time

def main():
    f = open("/tmp/daemon-log", "w")
    print os.getppid(),"ppid\n"
    print os.getpid(), "pid\n"
    while True:
	f.write("%s/n"%time.ctime(time.time()))
        f.flush()
        time.sleep(10)

if __name__ == "__main__":
	try:
	    pid = os.fork()
	    if pid > 0:
		    print "Daemon1 Pid %d" %pid
		    sys.exit(0)
	except OSError, e:
	    print >> sys.stderr, "fork #1 failed: %d (%s)" %(e.errno, e.strerror)
	    sys.exit(1)
	
	os.chdir("/")
	os.setsid()
	os.umask(0)

	try:
	    pid = os.fork()
	    if pid > 0:
		    print "Daemon Pid %d" %pid
		    sys.exit(0)
	except OSError, e:
	    print >> sys.stderr, "fork #2 failed: %d (%s)" %(e.errno, e.strerror)
	    sys.exit(1)

	main()
