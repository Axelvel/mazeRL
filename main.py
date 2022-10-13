import numpy as np
import qlearning
from maze import Maze
from colorama import init
import time


def main():

    # Colorama initialization
    init()

    # Importing the maze from the txt file
    list = [[]]

    with open('maze.txt') as f:
        i = 0
        for line in f:
            for char in line:
                if char == '\n':
                    list.append([])
                    i = i + 1
                else:
                    list[i].append(int(char))

    arr = np.array(list)

    #Initializing our MDP
    env = Maze(arr)
    
    # Running reinforcement learning algorithm
    print("\nRunning the algorithm...")
    start_time = time.time()
    ql = qlearning.QLearning(learning_rate=0.1, discount_factor=0.9, epsilon=0.1, epochs = 2000, environment=env)
    training_time = time.time() - start_time

    # Printing the path
    env.displayMaze(ql.path)
    ql.displayFitness()
   
    print("Training time : {}\n".format(training_time))
    

if __name__ == '__main__':
    main()
