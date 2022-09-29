from pylab import arange

timestep = None
Sresult = None
Iresult = None

def euler(beta, h):
    def initialize():
        global S, I, t, Sresult, Iresult, timestep
        S = 90
        I = 10
        t = 0
        Sresult = [S]
        Iresult = [I]
        timestep = [t]

    def observe():
        global S, I, t, Sresult, Iresult, timestep
        Sresult.append(S)
        Iresult.append(I)
        timestep.append(t)

    def update():
        global S, I, t, Sresult, Iresult, timestep
        nextS = S + (-beta * S * I + gamma * I) * h
        nextI = I + (beta * S * I - gamma * I) * h
        S = nextS
        I = nextI
        t = t + h

    gamma = 0.25

    initialize()
    for i in arange(0, h * 50, h):
        update()
        observe()

    global Sresult, Iresult, timestep
    return Sresult, Iresult, timestep
