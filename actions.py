from pprint import pprint

class Actions():
    def __init__(self, possibleActions=None):
        # UP RIGHT DOWN LEFT
        self.dir = \
            [
                {'id': 0, 'sym': '^', 'x': 0, 'y': 1},
                {'id': 1, 'sym': '>', 'x': 1, 'y': 0},
                {'id': 2, 'sym': 'v', 'x': 0, 'y': -1},
                {'id': 3, 'sym': '<', 'x': -1, 'y': 0}
            ]
        self.stay =  {'id': 0, 'sym': 'X', 'x': 0, 'y': 0}
        self.terminalAction = {'id': -1, 'sym': 'o', 'x': None, 'y': None}

        self.setPossibleActions(possibleActions)

    def setPossibleActions(self, possibleActions):
        actIdMap = {"L":-1,"R":+1,"O":+2,"S":None}
        if possibleActions is None:
            self.possibleActOffs = [actIdMap[p] for p in ["L", "R"]]
        else:
            self.possibleActOffs =  [actIdMap[p] for p in possibleActions]

    def isTerminalAction(self, action):
        return action['id'] == -1

    def getActions(self):
        return self.dir

    def getOtherPossibleActionsActions(self, action):
        actions = []
        for offs in self.possibleActOffs:
            if offs is None:
                actions.append(self.stay)
            else:
                actions.append(self.dir[(action['id'] + offs) % 4])
        return actions