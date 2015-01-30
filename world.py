import configparser
import pprint
import csv
from actions import Actions

class World():
    def __init__(self, map, terminals, probability):
        self.map = map[::-1] #[y][x]
        self.terminals = terminals
        self.actions = Actions()
        self.p1 = probability
        self.p2 = (1-self.p1)/2


    def getY(self):
        return len(self.map)

    def getX(self):
        return len(self.map[0])

    #state : tuple(x,y)
    def getReward(self, state):
        return self.map[state[1]][state[0]]

    def getActions(self, state):
        return self.actions.getActions() if state not in self.terminals else [self.actions.terminalAction]

    def bellmanOperator(self, state, action):
        if self.actions.isTerminalAction(action):
            return [(0, state)] #state is reahable for sure
        else:
            left, right = self.actions.getLeftRightActions(action)
            return [s for s in
                    [(self.p1, self.getNewState(state, action)),
                    (self.p2, self.getNewState(state, left)),
                    (self.p2, self.getNewState(state, right))]
                    if self.isStateReachable(s[1])]

    def getNewState(self, state, action):
        x=state[0]+action['x']
        y=state[1]+action['y']
        if x in range(self.getX()) and y in range(self.getY()):
            return x,y
        return state

    def isStateReachable(self, state):
        return True if self.map[state[1]][state[0]] is not None else False


