from pylab import arange

def euler(beta, h, h_count=50, gamma=0.25, s=90, i=10):
    s_result = [s]
    i_result = [i]
    timestep = [0]
    
    for _ in arange(0, h * h_count, h):
        s = s_result[-1]
        i = i_result[-1]

        s_result.append(s + (-beta * s * i + gamma * i) * h)
        i_result.append(i + (beta * s * i - gamma * i) * h)
        timestep.append(timestep[-1] + h)

    return s_result, i_result, timestep
