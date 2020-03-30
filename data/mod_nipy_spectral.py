import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import scipy.io

mat = scipy.io.loadmat('label_list.mat')
label_list = []
for l in range(59):
    label_list.append(str(mat['label_list'][0][l][0]))


ns = plt.cm.get_cmap("nipy_spectral")
cmap = mpl.colors.ListedColormap([ns(0), ns(1/59), ns(2 * 1/59), ns(3 * 1/59), ns(4 * 1/59), ns(5 * 1/59),
                                  ns(6 * 1/59), ns(7 * 1/59), ns(8 * 1/59), ns(9 * 1/59), ns(10 * 1/59),
                                  ns(11 * 1/59), ns(12 * 1/59), ns(13 * 1/59), ns(14 * 1/59), ns(15 * 1/59),
                                  ns(16 * 1/59), ns(17 * 1/59), ns(18 * 1/59), ns(19 * 1/59), ns(20 * 1/59),
                                  ns(21 * 1/59), ns(22 * 1/59), ns(23 * 1/59), ns(24 * 1/59), ns(25 * 1/59),
                                  ns(26 * 1/59), ns(27 * 1/59), ns(28 * 1/59), ns(29 * 1/59), ns(30 * 1/59),
                                  ns(31 * 1/59), ns(32 * 1/59), ns(33 * 1/59), ns(34 * 1/59), ns(35 * 1/59),
                                  ns(36 * 1/59), ns(37 * 1/59), ns(38 * 1/59), ns(39 * 1/59), ns(40 * 1/59),
                                  ns(41 * 1/59), ns(42 * 1/59), ns(43 * 1/59), ns(44 * 1/59), ns(45 * 1/59),
                                  ns(46 * 1/59), ns(47 * 1/59), ns(48 * 1/59), ns(49 * 1/59), ns(50 * 1/59),
                                  ns(51 * 1/59), ns(52 * 1/59), ns(53 * 1/59), ns(54 * 1/59), ns(55 * 1/59),
                                  ns(56*1/59), ns(57*1/59), ns(58*1/59)])

def show_colour_labels():
    fig, (ax1, ax2) = plt.subplots(1,2, figsize=(15, 12), gridspec_kw = {'width_ratios':[3, 0.1]}, constrained_layout = True)

    # Initializing the data
    num = 1000
    x2 = np.arange(0, 59, 1)
    y2 = np.ones(59)

    # Setting the Colormap
    ax1.scatter(x2, y2, c=x2, cmap=cmap)
    ax1.set_title('Nipy Spectral Discrete Colorbar', fontsize=16, weight='bold')

    # Setting the Discrete Colorbar
    bounds = np.arange(1,61,1)
    cb = mpl.colorbar.ColorbarBase(ax2, cmap=cmap,
                                    boundaries=bounds,
                                    ticks=bounds+0.5,spacing='proportional')
    cb.set_ticklabels(label_list)
    # Displaying the figure
    plt.show()

#show_colour_labels()
