import sys
from pprint import pprint
from mdp import Mdp
from uplotter import UPlotter

def main(argv):
    mdp = Mdp(argv[1], argv[2])
    u, pi = mdp.valueIterationSolve()
    try:
        if argv[3] == "plot":
            plot = UPlotter()
            plot.plot(u)
    except:
        pass

if __name__ == "__main__":
    main(sys.argv)
