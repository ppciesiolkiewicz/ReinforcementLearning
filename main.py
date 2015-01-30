import sys
from pprint import pprint
import Gnuplot
from mdp import Mdp


def main(argv):
    mdp = Mdp(argv[1], argv[2])
    u, pi = mdp.valueIterationSolve()
    gp = Gnuplot.Gnuplot(debug=1)
    gp('set style data linespoints')


if __name__ == "__main__":
    main(sys.argv)
