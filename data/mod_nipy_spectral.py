import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

ns = plt.cm.get_cmap("nipy_spectral")
cmap = mpl.colors.ListedColormap([ns(0.01818), ns(2 * 0.01818), ns(3 * 0.01818), ns(4 * 0.01818), ns(5 * 0.01818),
                                  ns(6 * 0.01818), ns(7 * 0.01818), ns(8 * 0.01818), ns(9 * 0.01818), ns(10 * 0.01818),
                                  ns(11 * 0.01818), ns(12 * 0.01818), ns(13 * 0.01818), ns(14 * 0.01818), ns(15 * 0.01818),
                                  ns(16 * 0.01818), ns(17 * 0.01818), ns(18 * 0.01818), ns(19 * 0.01818), ns(20 * 0.01818),
                                  ns(21 * 0.01818), ns(22 * 0.01818), ns(23 * 0.01818), ns(24 * 0.01818), ns(25 * 0.01818),
                                  ns(26 * 0.01818), ns(27 * 0.01818), ns(28 * 0.01818), ns(29 * 0.01818), ns(30 * 0.01818),
                                  ns(31 * 0.01818), ns(32 * 0.01818), ns(33 * 0.01818), ns(34 * 0.01818), ns(35 * 0.01818),
                                  ns(36 * 0.01818), ns(37 * 0.01818), ns(38 * 0.01818), ns(39 * 0.01818), ns(40 * 0.01818),
                                  ns(41 * 0.01818), ns(42 * 0.01818), ns(43 * 0.01818), ns(44 * 0.01818), ns(45 * 0.01818),
                                  ns(46 * 0.01818), ns(47 * 0.01818), ns(48 * 0.01818), ns(49 * 0.01818), ns(50 * 0.01818),
                                  ns(51 * 0.01818), ns(52 * 0.01818), ns(53 * 0.01818), ns(54 * 0.01818), ns(55 * 0.01818)])

fig, (ax1, ax2) = plt.subplots(1,2, figsize=(8, 5), gridspec_kw = {'width_ratios':[3, 0.1]})

# Initializing the data
num = 1000
x1 = np.linspace(-0.5,1,num) + (0.5 - np.random.rand(num))
y1 = np.linspace(-5,5,num) + (0.5 - np.random.rand(num))

# Setting the Colormap
ax1.scatter(x1, y1, c=x1, cmap=cmap)
ax1.set_title('Nipy Spectral Discrete Colorbar', fontsize=16, weight='bold')

# Setting the Discrete Colorbar
bounds = [1, 2, 6, 8]
mpl.colorbar.ColorbarBase(ax2, cmap=cmap,
                                boundaries=[0] + bounds + [10],
                                extend='both',
                                ticks=bounds,spacing='proportional')

# Displaying the figure
plt.show()