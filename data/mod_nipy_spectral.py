import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

ns = plt.cm.get_cmap("nipy_spectral")
cmap = mpl.colors.ListedColormap([ns(0) ,ns(56/100), ns(2 * 56/100), ns(3 * 56/100), ns(4 * 56/100), ns(5 * 56/100),
                                  ns(6 * 56/100), ns(7 * 56/100), ns(8 * 56/100), ns(9 * 56/100), ns(10 * 56/100),
                                  ns(11 * 56/100), ns(12 * 56/100), ns(13 * 56/100), ns(14 * 56/100), ns(15 * 56/100),
                                  ns(16 * 56/100), ns(17 * 56/100), ns(18 * 56/100), ns(19 * 56/100), ns(20 * 56/100),
                                  ns(21 * 56/100), ns(22 * 56/100), ns(23 * 56/100), ns(24 * 56/100), ns(25 * 56/100),
                                  ns(26 * 56/100), ns(27 * 56/100), ns(28 * 56/100), ns(29 * 56/100), ns(30 * 56/100),
                                  ns(31 * 56/100), ns(32 * 56/100), ns(33 * 56/100), ns(34 * 56/100), ns(35 * 56/100),
                                  ns(36 * 56/100), ns(37 * 56/100), ns(38 * 56/100), ns(39 * 56/100), ns(40 * 56/100),
                                  ns(41 * 56/100), ns(42 * 56/100), ns(43 * 56/100), ns(44 * 56/100), ns(45 * 56/100),
                                  ns(46 * 56/100), ns(47 * 56/100), ns(48 * 56/100), ns(49 * 56/100), ns(50 * 56/100),
                                  ns(51 * 56/100), ns(52 * 56/100), ns(53 * 56/100), ns(54 * 56/100), ns(55 * 56/100)])

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