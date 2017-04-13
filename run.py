import socket
import json
from World import World


#
# Handle game state
#
def handle_gamestate():
	w = World(data)

	# Adding targets
	targets = []
	if w.me['isdangerous']:
		for p in w.others:
			targets.append(p)
	else:
		for sp in w.superpellets:
			targets.append(sp)

	# Consuming targets
	if len(targets) > 0:
		target = targets.pop()
		move = w.getnextmove(target['x'], target['y'])

		# Make move
		if move:
			s.send(move)


#
# Socket, socket, ten dollah!
#
s = socket.socket()
host = socket.gethostname()
port = 54321
 
s.connect((host, port))

s.send(b"NAME MooG\n")


#
# Main loop
#
while True:
	raw = s.recv(4096)
	#print(raw)
	reply = raw.decode('ascii')
	parts = reply.strip().split("\n")

	for part in parts:
		data = json.loads( part )

		if data['messagetype'] == 'stateupdate':
			handle_gamestate()

		elif data['messagetype'] == 'welcome':
			print("Welcome!")

		elif data['messagetype'] == 'startofround':
			print("Start of round!")

		elif data['messagetype'] == 'dead':
			print("Dead")

		elif data['messagetype'] == 'endofround':
			print("End of round!")

		else:
			print("What!")
			print(data)
