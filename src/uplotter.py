import Gnuplot
from pprint import pprint
import operator

class UPlotter():
    def __init__(self):
        self.gp = Gnuplot.Gnuplot(debug=1)
        self.gp('set style data linespoints')

    def plot(self, u):
        #data = [[print(vals[key]) for key in vals] for t, vals in enumerate(u)] tpek nie ogarnal
        #data = ([ {key : [t, vals[key]]} for key in vals] for t, vals in enumerate(u)) CO TO KURWA JE?
        data = {}
        for t, vals in enumerate(u):
            for k in vals.keys():
                data[k] = [[t, vals[k]]] + data.get(k, [])
        self.gp.plot(*data.values())


