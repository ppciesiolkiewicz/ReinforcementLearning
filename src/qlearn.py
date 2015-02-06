
class Qlearn():


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

    def choose_action(self, state):
        if random.random() < self.epsilon: # exploration
            action = random.choice(self.actions)
        else:
            q = [self.getQ(state, a) for a in self.actions]
            maxQ = max(q)
            count = q.count(maxQ)
            if count > 1:
                best = [i for i in range(len(self.actions)) if q[i] == maxQ]
                i = random.choice(best)
            else:
                i = q.index(maxQ)

           action = self.actions[i]
        return action


    def solve(self):
        u, pi, t = self.init()
        w = self.world
        d = self.discountFactor
        e = self.epsilon

        print("Loaded world:")
        self.prettyPrintMap(self.world.rewards[::-1])

        while True:
            diff = 0
            u.append({})
            pi.append({})
            for y in range(w.getY()):
                for x in range(w.getX()):
                    state = (x, y)
                    if not w.isStateReachable(state):
                        continue


            if diff < e:
                break
            t += 1

        print("\nfinished after {0} iterations".format(t))
        print("\nU values: ")
        self.prettyPrintMap(self.toMatrix(u[-1]))
        print("\n Policy: ")
        self.prettyPrintMap(self.toMatrix(pi[-1]))


        return u, pi

    def prettyPrintMap(self, matrix):
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

