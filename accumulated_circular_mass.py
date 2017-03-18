import numpy as np
import math as mt
import matplotlib.pyplot as plt
import decimal as dec
from matplotlib.offsetbox import AnchoredText


class AccumulatedMass():

    def __init__(self, _mux, _muy, _mu, _radius, _particle_type, _massx, _massy, _massz, _particle_mass, _path_region):
        self.x              = _mux
        self.y              = _muy
        self.mu             = _mu
        self.radius         = _radius
        self.particle_type  = _particle_type
        self.massx          = _massx
        self.massy          = _massy
        self.massz          = _massz
        self.particle_mass  = _particle_mass
        self.path           = _path_region
        self.masel          = np.zeros(100)
        self.dimel          = np.zeros(100)
        self.masscirc       = np.zeros(len(_radius))


    def Acummulated(self):
        radius=self.radius
        for i in range(len(radius)):
            self.masscirc[i]= self.MassInCircle(radius[i])
            print 'Working...'

        np.savetxt(self.path + '/masas_acumuladas_circulos.txt', np.c_[radius, self.masscirc], fmt='%10.4g')
        return self.masscirc

    def MassInCircle(self, _radius):
        mass_acc_circ = 0.
        particle_type   = self.particle_type
        massx           = self.massx
        massy           = self.massy
        massz           = self.massz
        particle_mass   = self.particle_mass
        for i in range(len(massx)):
            if particle_type[i] == -1:
                zero_ = massx[i]** 2 + massy[i]** 2 - _radius** 2
                if zero_ <= 0:
                    mass_acc_circ = mass_acc_circ + particle_mass[i]

        return mass_acc_circ

    '''
    def AccumulatedMassCircPlot(self,_mulim):
        mu      = self.mu
        mass    = self.masscirc
        mulim   = _mulim
        index   = next(x[0] for x in enumerate(self.mu) if x[1] > mulim)
        x0      = np.array(mu[index - 1], mass[index - 1])
        x1      = np.array(mu[index], mass[index])
        a       = (mass[index]-mass[index-1])/(mu[index]-mu[index-1])
        b       = mass[index]-a*mu[index]
        masa_mulim = a* mulim+b

        ms = '%.3E' % dec.Decimal(str(masa_mulim))

        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 16, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        f, ax = plt.subplots(1, 1)
        anchored_text = AnchoredText('M$_{\star,\mu_{24}}$ =' + ms + ' $M_{\odot}$', loc=2)
        plt.axhline(y=masa_mulim, linewidth=1, color='r', linestyle='--')
        plt.scatter(mu, mass)
        ax.add_artist(anchored_text)
        plt.xlim(np.amin(mu), np.amax(mu))
        plt.ylim(9e+9, np.amax(mass))

        plt.xlabel("$\mu$ [$mag/arcsec^{2}$]")
        plt.ylabel('M$_{\star}$ [$M_{\odot}$]')
        plt.savefig(self.path + '/StellarMassvsMu_'+str(masa_mulim)+'.png')
        plt.show()


    def HalfRadius(self):
        mu      = self.mu
        mass    = self.masscirc
        dist    = self.radius

        index = next(x[0] for x in enumerate(mu) if x[1] > 24)
        x0 = np.array(mu[index - 1], mass[index - 1])
        x1 = np.array(mu[index], mass[index])
        a = (mass[index] - mass[index - 1]) / (mu[index] - mu[index - 1])
        b = mass[index] - a * mu[index]
        masa_24 = a * 24 + b
        masa_R50 = masa_24 / 2.

        index = next(x[0] for x in enumerate(mass) if x[1] > masa_R50)
        x0 = np.array(mass[index - 1], dist[index - 1])
        x1 = np.array(mass[index], dist[index])
        a = (dist[index] - dist[index - 1]) / (mass[index] - mass[index - 1])
        b = dist[index] - a * mass[index]
        R50 = b + a * (masa_R50)
        R50 = round(R50, 2)

        ms = '%.3E' % dec.Decimal(str(masa_24))
        mR50s = '%.3E' % dec.Decimal(str(masa_R50))

        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 16, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        f, ax = plt.subplots(1, 1)
        anchored_text = AnchoredText('R$_{50}$ =' + str(R50) + ' Kpc', loc=2)
        plt.axhline(y=R50, linewidth=1, color='r', linestyle='--')
        plt.scatter(mass, dist)
        ax.add_artist(anchored_text)
        plt.xlim(np.amin(mass), np.amax(mass))
        plt.ylim(0, 200)
        #plt.text(np.amax(mass) / 6., 160, 'M$_{\star,\mu_{24}}$ =  ' + ms + ' $M_{\odot}$')
        #plt.text(np.amax(mass) / 6., 145, 'M$_{R50}$ =  ' + mR50s + ' $M_{\odot}$')

        subpath = self.path[-11:]
        subpath = subpath[:6]
        plt.xlabel('M$_{\star}$ [$M_{\odot}$]')
        plt.ylabel('R [Kpc]')
        plt.savefig(self.path + '/_RvsMest.png')
        plt.show()
'''
