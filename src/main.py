import sys
from pprint import pprint
from mdp import Mdp
#from uplotter import UPlotter
import ast
from qlearn import Qlearn

def main(argv):
    #mdp = Mdp(argv[1], argv[2])
    mdp = Qlearn(argv[1], argv[2])
    u, pi = mdp.solve()
    try:
        fieldsToPlot = ast.literal_eval(argv[3])
    except:
        fieldsToPlot = None

    #plot = UPlotter()
    #plot.plot(u, fieldsToPlot)


if __name__ == "__main__":
    main(sys.argv)
