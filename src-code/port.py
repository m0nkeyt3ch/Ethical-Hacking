#!/bin/python

import sys
import socket
from datetime import datetime

#define target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1]) #translate host to IPv4
else:
    print("Invalid Syntax")
    print("python3 scanner.py <ip>")

print("Scanning target" + target)
print(str(datetime.now()))

try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target,port))
        if result == 0:
            print("port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()

except socket.gaierror:
    print("Hostname couldn't be resolved")
    sys.exit()

except socket.error:
    print("Couldn't connect to server")
    sys.exit()

