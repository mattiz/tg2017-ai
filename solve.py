import socket
import sys
import random
import json

 
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print 'Failed to create socket'
    sys.exit()
 
host = '127.0.0.1';
port = 54321;
 
s.connect((host, port))

while True: 
	reply = s.recv(4096)
	print json.dumps( reply, sort_keys=True, indent=4, separators=(',', ': '))

	moves = ['UP', 'DOWN', 'LEFT', 'RIGHT']
	move = moves[random.randint(0, 3)]
	s.sendall( move )
