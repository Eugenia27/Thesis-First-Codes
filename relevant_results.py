import numpy as np
import math as mt
import matplotlib.pyplot as plt
import decimal as dec
from matplotlib.offsetbox import AnchoredText
from pathlib import Path

class RelevantResults():

    def __init__(self, _mu, _radius, _masscirc, _mulimit, _path_region):
        self.mu             = _mu
        self.radius         = _radius
        self.masscirc       = _masscirc
        self.mulimit        = _mulimit
        self.mass_mulimit   = 0.0
        self.mulimitradius  = 0.0
        self.halfradius     = 0.0
        self.path           = _path_region


    def _MassInMulimit(self):
        mu      = self.mu
        mass    = self.masscirc
        mulimit = self.mulimit

        index = next(x[0] for x in enumerate(mu) if x[1] > 24)
        x0 = np.array(mu[index - 1], mass[index - 1])
        x1 = np.array(mu[index], mass[index])
        a  = (mass[index] - mass[index - 1]) / (mu[index] - mu[index - 1])
        b  = mass[index] - a * mu[index]
        self.mass_mulimit = a * mulimit + b

        ms = '%.3E' % dec.Decimal(str(self.mass_mulimit))

        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 16, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        textl = 'M$_{\mu_{24}}$ =' + ms + ' $M_{\odot}$'

        plt.axhline(y=self.mass_mulimit , linewidth=1, color='r', linestyle='--')
        plt.plot(mu, mass)
        plt.legend([textl],frameon=False)

        plt.xlim(np.amin(mu), np.amax(mu))
        plt.ylim(-0.01*np.amin(mass), 1.2*np.amax(mass))

        plt.xlabel("$\mu$ [$mag/arcsec^{2}$]")
        plt.ylabel('M$_{\star}$ [$M_{\odot}$]')

        plt.savefig(self.path + '/MassVsMu.png')

        plt.show()

        return self.mass_mulimit


    def _MuLimitSize(self):
        mu      = self.mu
        dist    = self.radius
        mulimit = self.mulimit

        index=next(x[0] for x in enumerate(mu) if x[1] > mulimit)
        x0=([dist[index-1],mu[index-1]])
        x1=([dist[index],mu[index]])
        x0,x1
        a= (x1[1]-x0[1])/(x1[0]-x0[0])
        b=x1[1]-a*x1[0]
        self.mulimitradius=(mulimit-b)/a
        self.mulimitradius=np.round(self.mulimitradius,2)

        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 16, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        textl ='R$_{\mu_{24}}$ =' + str(self.mulimitradius) + ' Kpc'

        plt.axvline(x=self.mulimitradius, linewidth=1, color='r', linestyle='--')
        plt.plot(dist,mu)
        plt.legend([textl],frameon=False)

        plt.ylim([np.amin(mu) - 0.3, np.amax(mu) + 0.3])
        plt.xlabel('R' + ' ' + ' ' + ' [$kpc$]')
        plt.ylabel("$\mu$ [$mag/arcsec^{2}$]")

        plt.savefig(self.path + '/MuVsR.png')
        plt.show()

        return self.mulimitradius


    def _HalfRadius(self):
        mass    = self.masscirc
        dist    = self.radius
        mu      = self.mu
        mulimit = self.mulimit

        index = next(x[0] for x in enumerate(mass) if x[1] > self.mass_mulimit/2.)
        x0 = np.array(mass[index - 1], dist[index - 1])
        x1 = np.array(mass[index], dist[index])
        a = (dist[index] - dist[index - 1]) / (mass[index] - mass[index - 1])
        b = dist[index] - a * mass[index]
        self.halfradius = b + a * ( self.mass_mulimit/2.)
        self.halfradius = round(self.halfradius, 2)

        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 16, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        textl ='R$_{50}$ =' + str(self.halfradius) + ' Kpc'

        plt.axhline(y=self.halfradius, linewidth=1, color='r', linestyle='--')
        plt.plot(mass, dist)
        plt.legend([textl],frameon=False)

        plt.xlim(np.amin(mass), np.amax(mass))
        plt.ylim(0, 200)

        plt.xlabel('M$_{\star}$ [$M_{\odot}$]')
        plt.ylabel('R [Kpc]')

        plt.savefig(self.path + '/RvsM.png')
        plt.show()

        return self.halfradius


    def PlotMassVSRadius(self,_reg,_snap,_progtype,_pathdir):
        mass    = self.masscirc
        dist    = self.radius

        ml= self._MassInMulimit()
        rl= self._MuLimitSize()
        hr= self._HalfRadius()

        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 16, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        ms = '%.3E' % dec.Decimal(str(ml))
        textm='M$_{\mu_{24}}$ =  ' + ms + ' $M_{\odot}$'
        texts='R$_{\mu_{24}}$ =  ' + str(rl) + ' Kpc'
        textr='R$_{50}$ =' + str(hr) + ' Kpc'

        plt.xlim(0,150)
        plt.ylim(np.min(mass),mass[77])

        plt.annotate(textm, xy=(1, 1), xytext=(-15, -275), fontsize=18,
                 xycoords='axes fraction', textcoords='offset points',
                 horizontalalignment='right', verticalalignment='bottom')

        plt.annotate(texts, xy=(1, 1), xytext=(-15, -300), fontsize=18,
                 xycoords='axes fraction', textcoords='offset points',
                 horizontalalignment='right', verticalalignment='bottom')

        plt.annotate(textr, xy=(1, 1), xytext=(-15, -325), fontsize=18,
                 xycoords='axes fraction', textcoords='offset points',
                 horizontalalignment='right', verticalalignment='bottom')

        plt.xlabel('R [Kpc]')
        plt.ylabel('M$_{\star}$ [$M_{\odot}$]')
        plt.title('D'+ str(_reg))

        regD= 'D'+str(_reg)

        myfile = open(_pathdir+_snap+'_'+_progtype+'_results.txt','a')
       # line = 'D'+str(_reg)+'\t'+_snap+'\t'+_progtype+'\t'+str(ml)+'\t'+str(rl)+'\t'+str(hr)
        myfile.write('{reg:4s} {snap:5s} {progt:4s} {mass:10.5g} {radius:10.2f} {half:10.2f} \n'.format(reg=regD,snap=_snap,progt=_progtype,
                                                                                                 mass=ml,radius=rl,half=hr))
        myfile.close()

        plt.plot(dist,mass,color='#006241')
        plt.scatter(dist,mass,color='#330035')
        plt.savefig(self.path + '/mvr.png')
        plt.show()

