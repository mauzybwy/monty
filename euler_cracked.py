from pylab import arange
from functools import reduce

def euler(beta, h, h_count=50, gamma=0.25, s_init=90, i_init=10):
    def evaluate(accum, _):
        s, i, t = accum
        return (
            s + [s[-1] + (-beta * s[-1] * i[-1] + gamma * i[-1]) * h],
            i + [i[-1] + (beta * s[-1] * i[-1] - gamma * i[-1]) * h],
            t + [t[-1] + h]
        )
        
    return reduce(evaluate, arange(0, h * h_count, h), ([s_init],[i_init],[0]))
