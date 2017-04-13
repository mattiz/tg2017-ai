from pathfinding.core.diagonal_movement import DiagonalMovement
from pathfinding.core.grid import Grid
from pathfinding.finder.a_star import AStarFinder
from collections import OrderedDict


class World:
    map = []
    me = {}
    others = {}
    pellets = []
    superpellets = []


    #
    # Constructor
    #
    def __init__(self, data):
        self.createMap(data)
        self.me = data['gamestate']['you']
        self.others = data['gamestate']['others']


    #
    # Create map
    #
    def createMap(self, data):
        newMap = []
        self.pellets = []
        self.superpellets = []

        for y, row in enumerate(data['gamestate']['map']['content']):
            newRow = []

            for x, col in enumerate(row):
                if col == '|':
                    newRow.append(1)
                else:
                    newRow.append(0)

                if col == 'o':
                    self.superpellets.append( {'x': x, 'y': y} )

                if col == '.':
                    self.pellets.append( {'x': x, 'y': y} )

            newMap.append(newRow)

        self.map = newMap


    #
    # Sort list of objects based on shortest path
    #
    def shortestPath(self, objects):
        result = []

        for o in objects[0:]:
            path = self.getpath(o['x'], o['y'])
            o['pathlength'] = len(path)
            result.append(o)

        return sorted( result, key=lambda k: k['pathlength'])

    #
    # Calculate paths to a target
    #
    def getpath(self, endx, endy):
        startx = self.me['x']
        starty = self.me['y']

        grid = Grid(matrix=self.map)
        finder = AStarFinder(diagonal_movement=DiagonalMovement.never)

        start = grid.node(startx, starty)
        end = grid.node(endx, endy)

        path, runs = finder.find_path(
            start,
            end,
            grid
        )

        #print('operations:', runs, 'path length:', len(path))
        #print(grid.grid_str(path=path, start=start, end=end))

        return path


    #
    # Get the next move to a target
    #
    def getnextmove(self, endx, endy):
        path = self.getpath(endx, endy)

        if len(path) > 1:
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
