from pprint import pprint
from actions import Actions


class World():
    def __init__(self, N, M, r, specials, p1, p2, possibleActions):
        self.buildMap(N, M, r, specials)
        self.p1 = p1
        self.p2 = p2

        self.actions = Actions(possibleActions)

    def buildMap(self, N, M, r, specials):
        self.rewards = [[r for x in range(N)] for y in range(M)]  # [y][x]
        self.terminals = []

        for s in specials:
            self.rewards[s[1]][s[0]] = specials[s][1]
            if specials[s][0] == "F":
                self.rewards[s[1]][s[0]] = None
            elif specials[s][0] == "G":
                self.terminals.append(s)
            elif specials[s][0] == "S":
                self.start = s



    def getY(self):
        return len(self.rewards)

    def getX(self):
        return len(self.rewards[0])

    # state : tuple(x,y)
    def getReward(self, state):
        return self.rewards[state[1]][state[0]]

    def getActions(self, state):
        return self.actions.getActions() if state not in self.terminals else [self.actions.terminalAction]

    def bellmanOperator(self, state, action):
        if self.actions.isTerminalAction(action):
            return [(0, state)]  #state is reachable for sure
        else:
            possibleAct = self.actions.getOtherPossibleActionsActions(action)
            probState = [(self.p2, self.getNewState(state, pa)) for pa in possibleAct] + [(self.p1, self.getNewState(state, action))]
            return [s for s in
                    probState
                    if self.isStateReachable(s[1])]

    def getNewState(self, state, action):
        x = state[0] + action['x']
        y = state[1] + action['y']
        if x in range(self.getX()) and y in range(self.getY()):
            return x, y
        return state

    def isStateReachable(self, state):
        return True if self.rewards[state[1]][state[0]] is not None else False


