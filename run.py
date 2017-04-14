import socket
import json
from World import World

lastTarget = None

#
# Handle game state
#
def handle_gamestate():
	global lastTarget

	w = World(data)

	# Adding targets
	targets = calculateTargets(w)

	# Consuming targets
	consumeTargets(targets, w)


#
# Consume targets
#
def consumeTargets(targets, w):
	if len(targets) > 0:
		target = aquireTarget(targets)
		move = w.getnextmove(target['x'], target['y'])

		# Make move
		if move:
			s.send(move)


#
# Calculate targets
#
def calculateTargets(w):
	targets = []

	if w.me['isdangerous']:
		for p in w.shortestPath(w.others):
			targets.append(p)

	elif len(w.superpellets) > 0:
		for sp in w.shortestPath(w.superpellets):
			targets.append(sp)

	elif len(w.pellets) > 0:
		for sp in w.pellets:
			targets.append(sp)

	return targets


#
# Aquire target
#
def aquireTarget(targets):
	global lastTarget

	hysteresis = 5
	target = targets[0]

	# Handle empty lastTarget
	if lastTarget == None:
		#print('lastTarget is None, returning target')
		newTarget = target

	# Handle lastTarget not in target list
	elif( len(list( filter( lambda t: t['x'] == lastTarget['x'] and t['y'] == lastTarget['y'], targets) )) <= 0 ):
		#print('lastTarget is not in list of targets')
		newTarget = target

	elif 'pathlength' in target and 'pathlength' in lastTarget and (target['pathlength']+hysteresis) < lastTarget['pathlength']:
		#print('targets pathlength is smaller than lasttarget')
		#print( (target['pathlength']+hysteresis), ' < ', lastTarget['pathlength'] )
		newTarget = target

	else:
		#print('lasttarget is still the best target')
		newTarget = lastTarget


	#for t in targets:
	#	print('T: ', t)
	#print('Last target: ', lastTarget)
	lastTarget = newTarget
	#print('New target: ', newTarget)
	#print('----------')
	return newTarget


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
