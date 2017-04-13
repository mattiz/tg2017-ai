import json

strings = [
    b'{"map":{"content":["||||||||||||||||||||||||||||","|............||............|","|.||||.|||||.||.|||||.||||.|","|o||||.|||||.||.|||||.||||o|","|.||||.|||||.||.|||||.||||.|","|..........................|","|.||||.||.||||||||.||.||||.|","|.||||.||.||||||||.||.||||.|","|......||....||....||......|","||||||.|||||_||_|||||.||||||","_____|.|||||_||_|||||.|_____","_____|.||__________||.|_____","_____|.||_|||--|||_||.|_____","||||||.||_|______|_||.||||||","______.___|______|___.______","||||||.||_|______|_||.||||||","_____|.||_|||--|||_||.|_____","_____|.||__________||.|_____","_____|.||_||||||||_||.|_____","||||||.||_||||||||_||.||||||","|............||............|","|.||||.|||||.||.|||||.||||.|","|.||||.|||||.||.|||||.||||.|","|o..||.......__.......||..o|","|||.||.||.||||||||.||.||.|||","|||.||.||.||||||||.||.||.|||","|......||....||....||......|","|.||||||||||.||.||||||||||.|","|.||||||||||.||.||||||||||.|","|..........................|","||||||||||||||||||||||||||||"],"height":31,"pelletsleft":240,"width":28},"messagetype":"welcome","you":{"id":0,"isdangerous":false,"score":0,"x":11,"y":13}}\n',
    b'{"messagetype":"startofround"}\n',
    b'{"gamestate":{"map":{"content":["||||||||||||||||||||||||||||","|............||............|","|.||||.|||||.||.|||||.||||.|","|o||||.|||||.||.|||||.||||o|","|.||||.|||||.||.|||||.||||.|","|..........................|","|.||||.||.||||||||.||.||||.|","|.||||.||.||||||||.||.||||.|","|......||....||....||......|","||||||.|||||_||_|||||.||||||","_____|.|||||_||_|||||.|_____","_____|.||__________||.|_____","_____|.||_|||--|||_||.|_____","||||||.||_|______|_||.||||||","______.___|______|___.______","||||||.||_|______|_||.||||||","_____|.||_|||--|||_||.|_____","_____|.||__________||.|_____","_____|.||_||||||||_||.|_____","||||||.||_||||||||_||.||||||","|............||............|","|.||||.|||||.||.|||||.||||.|","|.||||.|||||.||.|||||.||||.|","|o..||.......__.......||..o|","|||.||.||.||||||||.||.||.|||","|||.||.||.||||||||.||.||.|||","|......||....||....||......|","|.||||||||||.||.||||||||||.|","|.||||||||||.||.||||||||||.|","|..........................|","||||||||||||||||||||||||||||"],"height":31,"pelletsleft":240,"width":28},"others":[],"you":{"id":0,"isdangerous":false,"score":0,"x":12,"y":13}},"messagetype":"stateupdate"}\n',
    b'{"gamestate":{"map":{"content":["||||||||||||||||||||||||||||","|......||..........||......|","|_||||.||.||||||||.||.||||_|","|_||||.||.||||||||.||_||||_|","|__________________________|","|||_||_|||||_||_|||||_||_|||","__|_||_|||||_||_|||||_||_|__","|||_||_|||||_||_|||||_||_|||","____||_______||_______||____","|||_|||||_||||||||_|||||_|||","__|_|||||_||||||||_|||||_|__","__|______________________|__","__|_|||||_|||--|||_|||||_|__","__|_|||||_|______|_|||||_|__","__|_||____|______|____||_|__","__|_||_||_|______|_||_||_|__","|||_||_||_|||--|||_||_||_|||","_______||__________||_______","|||_||||||||_||_||||||||_|||","__|_||||||||_||_||||||||_|__","__|__________||__________|__","__|_|||||_||||||||_|||||_|__","|||_|||||_||||||||_|||||_|||","|__________________________|","|_||||_|||||_||_|||||_||||_|","|_||||_|||||_||_|||||_||||_|","|_||||_||____||____||_||||_|","|_||||_||_||||||||_||_||||_|","|_||||_||_||||||||_||_||||_|","|__________________________|","||||||||||||||||||||||||||||"],"height":31,"pelletsleft":29,"width":28},"others":[{"id":1000,"isdangerous":true,"score":0,"x":2,"y":4}],"you":{"id":0,"isdangerous":false,"score":231,"x":1,"y":4}},"messagetype":"stateupdate"}\n',
    b'{"messagetype":"dead"}\n{"messagetype":"endofround"}\n'
]

for s in strings:
    s = s.decode('ascii')
    parts = s.strip().split("\n")

    for part in parts:
        data = json.loads( str(part) )
        print(data['messagetype'])