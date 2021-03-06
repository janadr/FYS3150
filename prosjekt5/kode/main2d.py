import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import cm
import seaborn as sns
from matplotlib import ticker


sns.set()
sns.set_style("whitegrid")
sns.set_palette("husl")

datadir = "../data/"
figdir = "../figurer/"


data_forward = np.fromfile(datadir + "psi_bounded_sine_centered_2d.bin")
data_forward = np.reshape(data_forward,((1500,41,41)))
data_centered = np.fromfile(datadir + "psi_bounded_sine_centered_2d.bin")
data_centered = np.reshape(data_centered,((1500,41,41)))

fig, axes = plt.subplots(ncols=2, nrows=2, sharex=True, sharey=True)
fig.add_subplot(111, frameon=False)

plt.tick_params(labelcolor="none", top=False, bottom=False, left=False, right=False)
plt.grid(False)
plt.xlabel("Zonal extent", fontsize=14)
plt.ylabel("Meridional extent", fontsize=14)

x = np.linspace(0, 1, 41)
y = np.linspace(0, 1, 41)
x,y = np.meshgrid(x,y)

times = [50, 100, 150]
labels = ["t = 0"]
#ax[0,0].contourf(x, y, data_forward[0])
#ax[0,1].contourf(x, y, data_forward[499])
#ax[1,0].contourf(x, y, data_forward[999])
#ax[1,1].contourf(x, y, data_forward[1499])
#ax[1].contourf(x, y, data_centered[0])

fig.subplots_adjust(right=0.8)
levels = np.linspace(-1.5, 1.5, 12)
for ax, tindex in zip(axes.flat, [0, 499, 999, 1499]):
    im = ax.contourf(x, y, data_centered[tindex], cmap=cm.Greens_r,levels=levels, vmin=-1.1, vmax=1.1)

fig.subplots_adjust(right=0.8)
cbar_ax = fig.add_axes([0.85, 0.15, 0.05, 0.7])
cb = fig.colorbar(im, cax=cbar_ax)
tick_locator = ticker.MaxNLocator(nbins=11)
cb.locator = tick_locator
cb.update_ticks()
#plt.savefig(figdir + "bounded_sine_centered_2d.pdf")

plt.show()
