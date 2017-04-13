import socket
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

		# Adding targets
		targets = []

		if w.me['isdangerous']:
			for p in w.pellets:
				targets.append(p)
		else:
			for sp in w.superpellets:
				targets.append(sp)

		# Consuming targets
		if len(targets) > 0:
			target = targets.pop()
			move = w.getnextmove( target['x'], target['y'] )

		# Make move
		if move:
			s.send( move )
