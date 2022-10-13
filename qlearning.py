import numpy as np
import random
from utils import MoveCoordinates, Actions

class QLearning():

    def __init__(self, learning_rate, discount_factor, epsilon, epochs, environment):
        assert 0 < learning_rate < 1, "Learning rate must be between 0 and 1."
        assert 0 < discount_factor < 1, "Discount factor must be between 0 and 1."
        assert 0 < epsilon < 1, "Epsilon must be between 0 and 1."
        assert 0 < epochs, "Number of epoch must be greater than 0."

        self.environment = environment
        self.qtable = dict()
        self.learning_rate = learning_rate
        self.discount_factor = discount_factor
        self.epsilon = epsilon
        self.epochs = epochs
        self.reward = -1
        self.path = []

        self.run_algorithm(self.learning_rate, self.discount_factor)

    def run_algorithm(self, learning_rate=0.2, discount_factor=0.9):
        """ Running the QLearning algorithm """

        #Initializing qtable
        for state in self.environment.listStates():
                self.qtable[state] = [0, 0, 0, 0]

        self.path.append(self.environment.start)
        
        # Repeat for n number of episodes
        for i in range(self.epochs):

            state = self.environment.start

            #Repeat while exit not found
            while(state != self.environment.end):
                #Action selection strategy
                action, next_state = self.epsilon_greedy(state, self.epsilon)
                self.qtable[state][action] = self.qtable[state][action] + self.learning_rate * (self.environment.R(state, action) + self.discount_factor * max(self.qtable[next_state]) - self.qtable[state][action])
                state = next_state
                if i == self.epochs-1:
                    self.path.append(state)


    def epsilon_greedy(self, state, epsilon=0.1):
        if (random.random() < epsilon):
            # We pick a random action
            action = random.randint(0, 3)
        else:
            # We pick the action with the best Q-value
            action = np.argmax(self.qtable[state])
        next_state = self.environment.move(state, action)

        return action, next_state 

    def displayQ(self):
        print("\nQ-table generated:\n")
        for i in self.qtable:
            print(i, " : ", self.qtable[i])

    def displayPath(self):
        print("\nPath:\n")
        print(self.path[0], end=" ")
        for i in self.path[1:]:
            print("-> {}".format(i), end=" ")

    def displayFitness(self):
        print("\n\nPath length is : {}\n\n".format(len(self.path)))

