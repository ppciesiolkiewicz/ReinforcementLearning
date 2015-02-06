import Gnuplot
from pprint import pprint
import operator
from operator import itemgetter

class UPlotter():
    def __init__(self):
        self.gp = Gnuplot.Gnuplot(debug=1)
        self.gp('set style data linespoints')

    def plot(self, u, fieldsToPlot):
        print(fieldsToPlot)
        #data = [[print(vals[key]) for key in vals] for t, vals in enumerate(u)] tpek nie ogarnal
        #data = ([ {key : [t, vals[key]]} for key in vals] for t, vals in enumerate(u)) CO TO KURWA JE?
        data = {}

        Y= max(u[0].keys(),key=itemgetter(1))[1]+1
        X = max(u[0].keys(),key=itemgetter(0))[0]+1

        for t, vals in enumerate(u):
            for k in vals.keys():
                if( fieldsToPlot is None or k[0] + k[1]*X in fieldsToPlot):
                    if t == 0:
                        print("U for field {0} will be plotted".format(k))
                    data[k] = [[t, vals[k]]] + data.get(k, [])


        self.gp.plot(*data.values())


