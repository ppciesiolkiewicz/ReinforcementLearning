from world import World
import configparser
import ast

from pprint import pprint


class Mdp():
    def __init__(self, configfile, section):
        config = configparser.ConfigParser()
        config.read(configfile)
        cnf = dict(config.items(section))

        self.epsilon = ast.literal_eval(cnf['epsilon'])
        self.discountFactor = ast.literal_eval(cnf['discount_factor'])

        p1 = ast.literal_eval(cnf['probability1'])
        p2 = ast.literal_eval(cnf['probability2'])
        specials = ast.literal_eval(cnf['special_fields'])
        r = ast.literal_eval(cnf['r'])
        N = ast.literal_eval(cnf['n'])
        M = ast.literal_eval(cnf['m'])
        possibleActions = None
        try:
            possibleActions = ast.literal_eval(cnf['possible_actions'])
        except:
            pass

        self.world = World(N, M, r, specials, p1, p2, possibleActions)

    def init(self):
        u = []
        pi = []
        u.append({(x, y): 0 for x in range(self.world.getX()) for y in range(self.world.getY())})
        pi.append({(x, y): "" for x in range(self.world.getX()) for y in range(self.world.getY())})
        return u, pi, 1

    def valueIterationSolve(self):
        u, pi, t = self.init()
        w = self.world
        d = self.discountFactor
        e = self.epsilon

        while True:
            diff = 0
            u.append({})
            pi.append({})
            for y in range(w.getY()):
                for x in range(w.getX()):
                    state = (x, y)
                    if not w.isStateReachable(state):
                        continue

                    v = {}
                    for action in w.getActions(state):
                        v[action['sym']] = 0
                        for p, sNew in w.bellmanOperator(state, action):
                            v[action['sym']] += p * u[t - 1][sNew]

                    maxAct = max(v, key=lambda k: v[k])
                    pi[t][(x, y)] = maxAct

                    u[t][state] = w.getReward(state) + d * v[maxAct]
                    diff += abs(u[t][state] - u[t - 1][state])

            if diff < e:
                break
            t += 1
        self.prettyPrint2dList(self.toMatrix(u[-1]))
        self.prettyPrint2dList(self.toMatrix(pi[-1]))
        print("finished after {0} iterations".format(t))

        return u, pi

    def prettyPrint2dList(self, matrix):
        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table))

    def toMatrix(self, tuplesDict):
        m = [[None for x in range(self.world.getX())] for y in range(self.world.getY())]
        for t in tuplesDict:
            m[t[1]][t[0]] = tuplesDict[t]
        return m[::-1]

