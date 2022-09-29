# Import
from pylab import subplots, show
import euler_trash
import euler_better
import euler_cracked

# Vars to plot
betas = [.03, .06, .1]
hs = [.01, .5, 2]

# Setup Plot
fig, ax = subplots(nrows=3, ncols=3, figsize=(13,7))

# Plot
for (i, beta) in enumerate(betas):
    for (j, h) in enumerate(hs):

        # THREE EXAMPLES, UNCOMMENT TO TEST EACH
        # s_result, i_result, timestep = euler_trash.euler(beta, h)
        s_result, i_result, timestep = euler_better.euler(beta, h)
        # s_result, i_result, timestep = euler_cracked.euler(beta, h)
        
        ax[i,j].plot(timestep, i_result, 'r--')

# Display Plot
show()
