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
        a = (mass[index] - mass[index - 1]) / (mu[index] - mu[index - 1])
        b = mass[index] - a * mu[index]
        self.mass_mulimit = a * mulimit + b
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
        return self.halfradius


    def PlotMassVSRadius(self,_reg):
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
        plt.title('Reg '+ str(_reg))

        myfile = open('/home/meugenia/Documentos/masas_italia/results.txt','a')
        line = str(_reg)+'\t'+str(ml)+'\t'+str(rl)+'\t'+str(hr)
        myfile.write(line +'\n')

        plt.plot(dist,mass)
        plt.savefig(self.path + '/mvr.png')
        plt.show()

