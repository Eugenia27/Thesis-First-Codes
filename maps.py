import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from   matplotlib.colors import LogNorm
from   pylab import clabel
import numpy as np

class MapAndContours():

    def __init__(self, _pos1, _pos2,_mu,_path_region):
        self.x      = _pos1
        self.y      = _pos2
        self.mu     = np.array(_mu)
        self.path   = _path_region

    def Map(self):
        x = self.x
        y = self.y
        mu = self.mu

        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 16, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        plt.figure()

        x = np.linspace(-1 * (len(x) ** 0.5) / 2., (len(x) ** 0.5) / 2., 250)
        y = np.linspace(-1 * (len(y) ** 0.5) / 2., (len(y) ** 0.5) / 2., 250)
        N = int(len(mu) ** .5)
        x, y = np.meshgrid(x, y)
        mu = mu.reshape(N, N)
        mu = mu.transpose()
        cp = plt.contourf(x, y, mu, 100, vmin=16, vmax=40, cmap='Paired')

        plt.colorbar(cp, ticks=[16,19, 22, 24, 27, 30, 33, 36, 39], label="$\mu$ [$mag/arcsec^{2}$]")
        plt.title('Surface Brightness Map in XY plane')

        plt.savefig(self.path + '/maps.png')

        plt.show()

    def Contours(self):
        x = self.x
        y = self.y
        mu = self.mu

        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 12, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        plt.figure()
        N = int(len(mu) ** .5)
        mu = mu.reshape(N, N)
        mu = mu.transpose()
        plt.imshow(mu, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)),cmap=cm.gist_ncar, norm=LogNorm(), origin='lower	')

        levels = np.arange(20, 26, 1)
        CS = plt.contour(mu, levels,linewidths=2, extent=(np.amin(x), np.amax(x), np.amin(y), np.amax(y)), cmap=cm.gist_heat)
        clabel(CS, color="black", inline=True, fmt='%1.1f', fontsize=16, fontstyle="bold")

        plt.xlim(-40, 40)
        plt.ylim(-40, 40)
        plt.xlabel("x [Kpc]")
        plt.ylabel("y [Kpc]")
        plt.title("Surface Brightness Contours")
        #plt.savefig('output/contours.png')
        plt.show()