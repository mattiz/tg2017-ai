import json
from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder


class World:
    map = []
    me = {}
    superpellets = []

    def __init__(self, data):
        self.createMap(data)
        self.getMyPosition(data)

    def createMap(self, data):
        newMap = []

        for y, row in enumerate(data['gamestate']['map']['content']):
            newRow = []

            for x, col in enumerate(row):
                if col == '|':
                    newRow.append(1)
                else:
                    newRow.append(0)

                if col == 'o':
                    self.superpellets.append( {'x': x, 'y': y} )

            newMap.append(newRow)

        self.map = newMap

    def getMyPosition(self, data):
        self.me = data['gamestate']['you']

    def getpath(self, startx, starty, endx, endy):
        grid = Grid(matrix=self.map)

        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

        path, runs = finder.find_path(
            grid.node(startx, starty),
            grid.node(endx, endy),
            grid
        )

        return path

    def getnextmove(self, startx, starty, endx, endy):
        path = self.getpath(startx, starty, endx, endy)

        x1 = path[0][0]
        y1 = path[0][1]
        x2 = path[1][0]
        y2 = path[1][1]

        if x2 > x1:
            return b'RIGHT'

        if( x2 < x1 ):
            return b'LEFT'

        if( y2 > y1 ):
            return b'DOWN'

        if( y2 < y1 ):
            return b'UP'




#str = '{"map":{"content":["||||||||||||||||||||||||||||","|............||............|","|.||||.|||||.||.|||||.||||.|","|o||||.|||||.||.|||||.||||o|","|.||||.|||||.||.|||||.||||.|","|..........................|","|.||||.||.||||||||.||.||||.|","|.||||.||.||||||||.||.||||.|","|......||....||....||......|","||||||.|||||_||_|||||.||||||","_____|.|||||_||_|||||.|_____","_____|.||__________||.|_____","_____|.||_|||--|||_||.|_____","||||||.||_|______|_||.||||||","______.___|______|___.______","||||||.||_|______|_||.||||||","_____|.||_|||--|||_||.|_____","_____|.||__________||.|_____","_____|.||_||||||||_||.|_____","||||||.||_||||||||_||.||||||","|............||............|","|.||||.|||||.||.|||||.||||.|","|.||||.|||||.||.|||||.||||.|","|o..||.......__.......||..o|","|||.||.||.||||||||.||.||.|||","|||.||.||.||||||||.||.||.|||","|......||....||....||......|","|.||||||||||.||.||||||||||.|","|.||||||||||.||.||||||||||.|","|..........................|","||||||||||||||||||||||||||||"],"height":31,"pelletsleft":240,"width":28},"messagetype":"welcome","you":{"id":0,"isdangerous":false,"score":0,"x":11,"y":13}}'
#str = '{"gamestate":{"map":{"content":["||||||||||||||||||||||||||||","|............||............|","|.||||.|||||.||.|||||.||||.|","|o||||.|||||.||.|||||.||||o|","|.||||.|||||.||.|||||.||||.|","|..........................|","|.||||.||.||||||||.||.||||.|","|.||||.||.||||||||.||.||||.|","|......||....||....||......|","||||||.|||||_||_|||||.||||||","_____|.|||||_||_|||||.|_____","_____|.||__________||.|_____","_____|.||_|||--|||_||.|_____","||||||.||_|______|_||.||||||","______.___|______|___.______","||||||.||_|______|_||.||||||","_____|.||_|||--|||_||.|_____","_____|.||__________||.|_____","_____|.||_||||||||_||.|_____","||||||.||_||||||||_||.||||||","|............||............|","|.||||.|||||.||.|||||.||||.|","|.||||.|||||.||.|||||.||||.|","|o..||.......__.......||..o|","|||.||.||.||||||||.||.||.|||","|||.||.||.||||||||.||.||.|||","|......||....||....||......|","|.||||||||||.||.||||||||||.|","|.||||||||||.||.||||||||||.|","|..........................|","||||||||||||||||||||||||||||"],"height":31,"pelletsleft":240,"width":28},"others":[],"you":{"id":0,"isdangerous":false,"score":0,"x":12,"y":13}},"messagetype":"stateupdate"}'

#data = json.loads(str)
#w = World( data )

#print( w.getnextmove( 11, 13, 1, 3 ) )

#pretty = json.dumps(data, sort_keys=True, indent=4, separators=(',', ': '))
#print(pretty)