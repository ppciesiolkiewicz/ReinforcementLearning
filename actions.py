import random


# Action returns
class Actions():
    def __init__(self):
        # UP RIGHT DOWN LEFT
        self.dir = \
            [
                {'id': 0, 'sym': '^', 'x': 0, 'y': 1},
                {'id': 1, 'sym': '>', 'x': 1, 'y': 0},
                {'id': 2, 'sym': 'v', 'x': 0, 'y': -1},
                {'id': 3, 'sym': '<', 'x': -1, 'y': 0}
            ]
        self.terminalAction = {'id': -1, 'sym': 'o', 'x': None, 'y': None}

    def isTerminalAction(self, action):
        return action['id'] == -1

    def getActions(self):
        return self.dir

    def getLeftRightActions(self, action):
        return self.dir[(action['id'] + 1) % 4], self.dir[(action['id'] - 1) % 4]