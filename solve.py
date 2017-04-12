import socket
import sys
import random
import json


s = socket.socket()
host = socket.gethostname()
port = 54321
 
s.connect((host, port))

s.send(b"NAME MooG\n")

while True: 
	reply = s.recv(4096)
	#print( json.dumps( reply, sort_keys=True, indent=4, separators=(',', ': ')))

	print(reply)

	moves = [b'UP', b'DOWN', b'LEFT', b'RIGHT']
	move = moves[random.randint(0, 3)]
	s.send( move )
