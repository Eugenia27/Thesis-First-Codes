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
        plt.plot(self.r, self.mu, linestyle='--', marker='^', color='r')

        plt.ylabel("$\mu$ [$mag/arcsec^{2}$]")

        if self.log == False:
            plt.xlabel("R [Kpc]")
            plt.savefig(self.path + '/sb_profile.png')

        if self.log == True:
            plt.xlabel("log$_{10}$R [Kpc]")
            plt.savefig(self.path + '/sb_profile_log.png')

        plt.show()

    def Size(self):
        index = next(x[0] for x in enumerate(self.mu) if x[1] > 24)
        x0 = ([self.r[index - 1], self.mu[index - 1]])
        x1 = ([self.r[index], self.mu[index]])
        x0, x1
        a = (x1[1] - x0[1]) / (x1[0] - x0[0])
        b = x1[1] - a * x1[0]
        r_24 = (24 - b) / a
        r_24 = np.round(r_24, 2)
        r_24_s = str(r_24)
        absc = np.arange(np.amin(self.r), np.amax(self.r))
        orde = b + a * absc

        plt.axvline(x=r_24, linewidth=1, color='r', linestyle='--')
        plt.scatter(self.r, self.mu)
        plt.ylim([np.amin(self.mu) - 0.3, np.amax(self.mu) + 0.3])
        plt.xlabel('a' + ' ' + ' ' + ' [$kpc$]')
        plt.ylabel("$\mu$ [$mag/arcsec^{2}$]")
        plt.text(r_24 - 39, 22, 'a$_{\mu_{24}}$ = ' + r_24_s + ' kpc')
        #plt.savefig(self.path + '/muvsa.png')
        #plt.show()