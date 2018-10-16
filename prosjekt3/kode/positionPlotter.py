from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
import numpy as np
import sys
import glob
import seaborn as sns

sns.set()
sns.set_style("white")
sns.set_palette("husl")
#plt.rc('text', usetex=True)

def plotPlanet(ax, filename):
    data = np.loadtxt(filename)
    name = filename.split("/")[-1][:-4]
    x = data[:,0]; y = data[:,1]; z = data[:,2];
    ax.plot3D(x,y,z,label=name)
    #ax.plot(x,y,label=name)

def plotSystem(ax, path):
    files = glob.glob(path+"/*.dat")
    for filename in files:
        plotPlanet(ax, filename)


fig = plt.figure()
ax = plt.axes(projection='3d')
#ax = fig.add_subplot(1,1,1)

plotSystem(ax, "../data/solarsystem")

ax.legend()
ax.grid(False)
plt.axis('equal')
#plt.axis('off')

plt.show()
