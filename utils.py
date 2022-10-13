from enum import Enum, IntEnum


class MoveCoordinates(Enum):

    UP = (-1, 0)
    RIGHT = (0, 1)
    DOWN = (1, 0)
    LEFT = (0, -1)

class Actions(Enum):
    
    UP = 0
    RIGHT = 1
    DOWN = 2
    LEFT = 3

class CellType(IntEnum):

    EMPTY = 0
    WALL = 1
