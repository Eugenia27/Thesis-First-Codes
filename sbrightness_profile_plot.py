import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from    matplotlib.colors import LogNorm
import numpy as np


class SurfaceBrightnessPlot():

    def __init__(self, _r, _mu, _log, _path_region):
        self.r = _r
        self.mu = _mu
        self.log = _log
        self.path = _path_region

    def Plot(self):
        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 16, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        N = 50
        colors = np.random.rand(N)
        area = np.pi * (15 * np.random.rand(N)) ** 2
        self.mu = self.mu[self.mu > 0]
        self.r = self.r[self.mu > 0]

        plt.figure()
        plt.ylim([np.amax(self.mu) + 0.5, np.amin(self.mu) - 0.5])
        plt.plot(self.r, self.mu)
        plt.scatter(self.r, self.mu, color='red')

        plt.ylabel("$\mu$ [$mag/arcsec^{2}$]")
        plt.title('Surface Brightness vs R')

        if self.log == False:
            plt.xlabel("R [Kpc]")
            plt.savefig(self.path + '/sb_profile.png')

        if self.log == True:
            plt.xlabel("log$_{10}$R [Kpc]")
            plt.savefig(self.path + '/sb_profile_log.png')

        plt.show()
'''

        '''