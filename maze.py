
import numpy as np
from utils import MoveCoordinates, Actions, CellType
from colorama import Fore, Back

class Maze:

    def __init__(self, maze) -> None:
        self.maze = maze
        self.start = (0, 0)
        self.end = (np.shape(self.maze)[0] - 1, np.shape(self.maze)[1] - 1)

    def move(self, state, action):
        new_pos = self.T(state, action)
        return new_pos

    def R(self, state, action):
        return -1

    def T(self, state, action):
        new_pos = tuple(map(sum, zip(state, MoveCoordinates[Actions(action).name].value)))
        
        if (0 <= new_pos[0] < np.shape(self.maze)[0] and 0 <= new_pos[1] < np.shape(self.maze)[1]):
            # if cell is empty
            if (self.maze[new_pos] != CellType.WALL):
                # Cell is empty
                return new_pos
        return state

    def listAction(self):
        return range(len(MoveCoordinates))

    def listStates(self):
        for x in range(np.shape(self.maze)[0]):
            for y in range(np.shape(self.maze)[1]):
                yield (x, y)

    def displayMaze(self, path):
        print("\nMaze:\n")
        for i in range(np.shape(self.maze)[0]):
            print("[", end=" ")
            for j in range(np.shape(self.maze)[1]):
                x = self.maze[i][j]
                if (self.maze[i][j] == 1):
                    print(Back.RED + str(x) + Back.RESET, end=" ")
                elif path != None and (i, j) in path:
                    print(Back.GREEN + str(x) + Back.RESET, end=" ")       
                else: 
                    print(str(x), end=" ")
            print("]")
        print("\n")


    

