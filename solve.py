import socket
import random
import json
from World import World


s = socket.socket()
host = socket.gethostname()
port = 54321
 
s.connect((host, port))

s.send(b"NAME MooG\n")

while True: 
	reply = s.recv(4096)

	d = str(reply)[2:-3]
	data = json.loads( d )

	if 'gamestate' in data:
		w = World( data )
		move = w.getnextmove( w.me['x'], w.me['y'], w.superpellets[0]['x'], w.superpellets[0]['y'] )
		s.send( move )
