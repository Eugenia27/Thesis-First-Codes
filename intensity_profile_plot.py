import matplotlib
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from    matplotlib.colors import LogNorm
import numpy as np


class SpecificIntensityPlot():

    def __init__(self, _r, _ie, _log, _path_region):
        self.r      = _r
        self.ie     = _ie
        self.log    = _log
        self.path   = _path_region

    def Plot(self):
        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 16, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        N = 50
        np.random.rand(N)
        np.pi * (15 * np.random.rand(N)) ** 2

        plt.figure()
        plt.ylim([-2*np.amin(self.ie), np.amax(self.ie) + 0.05*np.amax(self.ie)])
        #plt.plot(self.r, self.ie, linestyle='--', marker='^', color='r)
        plt.plot(self.r, self.ie)

        plt.ylabel("I$_{e}$ [$erg s^{-1} cm^{-2} Hz^{-1} sr^{-1} $]")
        plt.title('Specific Intensity vs R')

        if self.log == False:
            plt.xlabel("R [Kpc]")
            plt.savefig(self.path+'/ie_profile.pdf')

        if self.log == True:
            plt.xlabel("log$_{10}$R [Kpc]")
            plt.savefig(self.path+'/ie_profile_log.pdf')

        plt.show()