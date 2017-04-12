import json

str = '{"map":{"content":["||||||||||||||||||||||||||||","|............||............|","|.||||.|||||.||.|||||.||||.|","|o||||.|||||.||.|||||.||||o|","|.||||.|||||.||.|||||.||||.|","|..........................|","|.||||.||.||||||||.||.||||.|","|.||||.||.||||||||.||.||||.|","|......||....||....||......|","||||||.|||||_||_|||||.||||||","_____|.|||||_||_|||||.|_____","_____|.||__________||.|_____","_____|.||_|||--|||_||.|_____","||||||.||_|______|_||.||||||","______.___|______|___.______","||||||.||_|______|_||.||||||","_____|.||_|||--|||_||.|_____","_____|.||__________||.|_____","_____|.||_||||||||_||.|_____","||||||.||_||||||||_||.||||||","|............||............|","|.||||.|||||.||.|||||.||||.|","|.||||.|||||.||.|||||.||||.|","|o..||.......__.......||..o|","|||.||.||.||||||||.||.||.|||","|||.||.||.||||||||.||.||.|||","|......||....||....||......|","|.||||||||||.||.||||||||||.|","|.||||||||||.||.||||||||||.|","|..........................|","||||||||||||||||||||||||||||"],"height":31,"pelletsleft":240,"width":28},"messagetype":"welcome","you":{"id":0,"isdangerous":false,"score":0,"x":11,"y":13}}'

data = json.loads(str)

map = []

for y, row in enumerate(data['map']['content']):
    newRow = []

    for x, col in enumerate(row):
        if col == '|':
            newRow.append(1)
        else:
            newRow.append(0)

        if col == 'o':
            print('x: ', x, ', y: ', y)

    map.append(newRow)


print( data['map']['content'] )
print( map )

#pretty = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
#print(pretty)