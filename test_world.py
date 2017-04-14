import json
from World import World

raw = b'{"gamestate":{"map":{"content":["||||||||||||||||||||||||||||","|____________||____________|","|_||||_|||||_||_|||||_||||_|","|_||||_|||||_||_|||||_||||_|","|_||||_|||||_||_|||||_||||_|","|__________________________|","|_||||_||_||||||||_||_||||.|","|_||||_||_||||||||_||_||||.|","|______||____||____||______|","||||||_|||||_||_|||||_||||||","_____|_|||||_||_|||||_|_____","_____|_||__________||_|_____","_____|_||_|||--|||_||_|_____","||||||_||_|______|_||_||||||","__________|______|__________","||||||_||_|______|_||_||||||","_____|_||_|||--|||_||_|_____","_____|_||__________||_|_____","_____|_||_||||||||_||_|_____","||||||_||_||||||||_||_||||||","|____________||____________|","|_||||_|||||_||_|||||_||||_|","|_||||_|||||_||_|||||_||||_|","|___||________________||___|","|||_||_||_||||||||_||_||_|||","|||_||_||_||||||||_||_||_|||","|______||____||____||______|","|_||||||||||_||_||||||||||_|","|_||||||||||_||_||||||||||_|","|__________________________|","||||||||||||||||||||||||||||"],"height":31,"pelletsleft":2,"width":28},"others":[{"id":0,"isdangerous":false,"score":4,"x":14,"y":15},{"id":1000,"isdangerous":true,"score":0,"x":26,"y":4}],"you":{"id":1,"isdangerous":false,"score":227,"x":18,"y":5}},"messagetype":"stateupdate"}\n'

data = json.loads( raw.decode('ascii') )
w = World(data)
w.printMap()