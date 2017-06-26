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

        x = np.linspace(-1 * (len(x) ** 0.5) , (len(x) ** 0.5), 250)
        y = np.linspace(-1 * (len(y) ** 0.5) , (len(y) ** 0.5), 250)

        N = int(len(mu) ** .5)
        x, y = np.meshgrid(x, y)
        mu = mu.reshape(N, N)
        mu = mu.transpose()

        levels = (16., 17., 18., 19., 20., 20.5, 21., 21.5, 22., 22.5, 23., 23.5, 24.,24.5, 25., 26., 30., 40., 50.)

        fig, ax = plt.subplots()
        plot = ax.contourf(x, y, mu, levels=levels, colors=['#FFFCC3',
                                                            '#FFEBA5',
                                                            '#F5D467',
                                                            '#FFF446',
                                                            '#FFD426',
                                                            '#FFA61F',
                                                            '#FF8000',
                                                            '#E8A5FF',
                                                            '#D45BFF',
                                                            '#BC00FF',
                                                            '#862DA6',
                                                            '#810090',
                                                            '#330035',
                                                            '#00EC96',
                                                            '#00BC77',
                                                            '#028957',
                                                            '#006241',
                                                            '#003624',
                                                            ])

        cbar = fig.colorbar(plot, ticks=levels)
        cbar.set_label("$\mu$ [$mag/arcsec^{2}$]")

        #cp = plt.contourf(x, y, mu, 100, vmin=16, vmax=40, cmap='Paired')

        #plt.colorbar(cp, ticksX=[16,19, 22, 24, 27, 30, 33, 36, 39], label="$\mu$ [$mag/arcsec^{2}$]")
        plt.title('Surface Brightness Map in XY plane')
        plt.xlabel("x [Kpc]")
        plt.ylabel("y [Kpc]")

        plt.savefig(self.path + '/maps.png')
        plt.savefig(self.path + '/maps.pdf', format='pdf',dpi=1300)

        plt.show()

    def Contours(self):
        x = self.x
        y = self.y
        mu = self.mu

        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 16, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        matplotlib.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        x = np.linspace(-1 * (len(x) ** 0.5) , (len(x) ** 0.5), 250)
        y = np.linspace(-1 * (len(y) ** 0.5) , (len(y) ** 0.5), 250)

        N = int(len(mu) ** .5)
        x, y = np.meshgrid(x, y)
        mu = mu.reshape(N, N)
        mu = mu.transpose()

        levels = (16, 18, 20, 21, 22, 23, 24, 25)

        fig, ax = plt.subplots()
        ax.patch.set_facecolor('#DEFFD5')
        cs = ax.contour(x, y, mu, levels=levels, colors=['#FFFCC3',
                                                         '#F5D467',
                                                         '#FFD426',
                                                         '#FF8000',
                                                         '#D45BFF',
                                                         '#862DA6',
                                                         '#330035',
                                                         '#00BC77',
                                                         ], linewidths=2)

        cbar = fig.colorbar(cs, ticks=[16, 18, 20, 21, 22, 23, 24, 25])
        plt.xlim(-150, 150)
        plt.ylim(-150, 150)

        #plt.xlim(-125, 125)
        #plt.ylim(-125, 125)
        plt.xlabel("x [Kpc]")
        plt.ylabel("y [Kpc]")
        plt.title("Surface Brightness Contours")
        #plt.savefig('output/contours.png')
        plt.savefig(self.path + '/contoursmaps.png')
        plt.savefig(self.path + '/contoursmaps.pdf', format='pdf',dpi=1300)
        plt.show()