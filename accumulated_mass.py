import numpy as np
import math as mt
import matplotlib.pyplot as plt
import decimal as dec
from matplotlib.offsetbox import AnchoredText


class AccumulatedMass():

    def __init__(self, _x, _y, _mu, _sma, _path_region, _path_input):
        self.x = _x
        self.y = _y
        self.mu = _mu
        self.sma = _sma
        self.path = _path_region
        self.pathin = _path_input
        #self.sma = np.zeros(100)
        self.masel = np.zeros(100)
        self.dimel = np.zeros(100)

    def Acumuladas(self):
        sma = self.sma
        elli = np.zeros(len(sma))
        pa   = np.zeros(len(sma))

        #print sma
        #print elli
        #print pa
        #sma, elli, pa = np.loadtxt(self.path + '/elipses.txt', usecols=[0, 1, 2], unpack=True)
        self.masel = np.zeros(len(sma))
        self.dimel = np.zeros(len(sma))
        for i in range(len(sma)):
            xx, yy = self._Focus(sma[i], elli[i])
            focus = self.Rotation_Matrix(xx, yy, pa[i])
            self.masel[i], self.dimel[i] = self.Ellipse(focus, sma[i])
            print 'Working...'

        np.savetxt(self.path + '/masas.txt', np.c_[self.masel, self.dimel], fmt='%10.4g')
        return self.sma, self.masel, self.dimel

    def Pa_To_Theta(self, pa):
        if pa >= 0 and pa < 270:
            theta = pa + 90
        if pa >= 270 and pa < 360:
            theta = pa - 270
        return theta

    def _Focus(self, _sma, _ell):
        c = _sma * _ell
        xx = np.array([-c, c])
        yy = np.array([0, 0])
        return xx, yy

    def Rotation_Matrix(self, _x, _y, _theta):
        _theta = _theta * np.pi / 180.
        R_theta = np.array([[np.cos(_theta), -1 * np.sin(_theta)],
                            [np.sin(_theta), np.cos(_theta)]])
        for i in range(len(_x)):
            point = np.array([_x, _y])
            rot_point = R_theta.dot(point)
        return rot_point

    def Distance(self, _x1, _x2, _y1, _y2):
        distance_ = mt.sqrt((_x1 - _x2) ** 2 + (_y1 - _y2) ** 2)
        return distance_

    def Ellipse(self, rot_point, sma):
        j = 0
        masst = 0.
        type_p, xx, yy, zz, mass_p = np.loadtxt(self.pathin, skiprows=1, usecols=[0, 1, 2, 3, 8], unpack=True)
        for i in range(len(xx)):
            if type_p[i] == -1:
                # if mass_p[i] != 0:
                # print xx[i]
                df1 = self.Distance(xx[i], 0, yy[i], 0)
                # zero_ = df1+df2-2*sma
                zero_ = xx[i] ** 2 + yy[i] ** 2 - sma ** 2
                if zero_ <= 0:
                    masst = masst + mass_p[i]
                    j = j + 1
                    # print j
        return masst, j

    def _MassPlot(self):
        masas, dimens = np.loadtxt(self.path + '/masas.txt', usecols=[0, 1], unpack=True)
        dist, mu_ = np.loadtxt(self.path + '/mean_mu_nlog.txt', usecols=[0, 1], unpack=True)

        index = next(x[0] for x in enumerate(mu_) if x[1] > 24)
        x0 = np.array(mu_[index - 1], masas[index - 1])
        x1 = np.array(mu_[index], masas[index])
        a = (masas[index] - masas[index - 1]) / (mu_[index] - mu_[index - 1])
        b = masas[index] - a * mu_[index]
        masa_24 = a * 24 + b

        ms = '%.3E' % dec.Decimal(str(masa_24))

        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 16, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        f, ax = plt.subplots(1, 1)
        anchored_text = AnchoredText('M$_{\star,\mu_{24}}$ =' + ms + ' $M_{\odot}$', loc=2)
        # ax.spines['bottom'].set_color('red')
        # ax.spines['top'].set_color('red')
        plt.axhline(y=masa_24, linewidth=1, color='r', linestyle='--')
        plt.scatter(mu_, masas)
        ax.add_artist(anchored_text)
        plt.xlim(np.amin(mu_), np.amax(mu_))
        plt.ylim(9e+9, np.amax(masas))
        # plt.text(20,masas[len(masas)/2], 'M$_{\star,\mu_{24}}$ =  '+ms+' $M_{\odot}$')



        plt.xlabel("$\mu$ [$mag/arcsec^{2}$]")
        plt.ylabel('M$_{\star}$ [$M_{\odot}$]')
        plt.savefig(self.path + '/Mvsmu.png')
        plt.show()

    def _R50(self):
        masas, dimens = np.loadtxt(self.path + '/masas.txt', usecols=[0, 1], unpack=True)
        dist, mu_ = np.loadtxt(self.path + '/mean_mu_nlog.txt', usecols=[0, 1], unpack=True)

        masas, dimens = np.loadtxt(self.path + '/masas.txt', usecols=[0, 1], unpack=True)
        dist, mu_ = np.loadtxt(self.path + '/mean_mu_nlog.txt', usecols=[0, 1], unpack=True)

        index = next(x[0] for x in enumerate(mu_) if x[1] > 24)
        x0 = np.array(mu_[index - 1], masas[index - 1])
        x1 = np.array(mu_[index], masas[index])
        a = (masas[index] - masas[index - 1]) / (mu_[index] - mu_[index - 1])
        b = masas[index] - a * mu_[index]
        masa_24 = a * 24 + b
        masa_R50 = masa_24 / 2.

        index = next(x[0] for x in enumerate(masas) if x[1] > masa_R50)
        x0 = np.array(masas[index - 1], dist[index - 1])
        x1 = np.array(masas[index], dist[index])
        a = (dist[index] - dist[index - 1]) / (masas[index] - masas[index - 1])
        b = dist[index] - a * masas[index]
        R50 = b + a * (masa_R50)
        R50 = round(R50, 2)

        print masa_24, masa_R50
        ms = '%.3E' % dec.Decimal(str(masa_24))
        mR50s = '%.3E' % dec.Decimal(str(masa_R50))

        plt.rc('text', usetex=True)
        font = {'family': 'serif', 'size': 16, 'serif': ['computer modern roman']}
        plt.rc('font', **font)
        plt.rc('legend', **{'fontsize': 14})
        plt.rcParams['text.latex.preamble'] = [r'\usepackage{amsmath}']

        f, ax = plt.subplots(1, 1)
        anchored_text = AnchoredText('R$_{50}$ =' + str(R50) + ' Kpc', loc=2)
        # ax.spines['bottom'].set_color('red')
        # ax.spines['top'].set_color('red')
        plt.axhline(y=R50, linewidth=1, color='r', linestyle='--')
        plt.scatter(masas, dist)
        ax.add_artist(anchored_text)
        plt.xlim(np.amin(masas), np.amax(masas))
        plt.ylim(0, 200)
        plt.text(np.amax(masas) / 6., 160, 'M$_{\star,\mu_{24}}$ =  ' + ms + ' $M_{\odot}$')
        plt.text(np.amax(masas) / 6., 145, 'M$_{R50}$ =  ' + mR50s + ' $M_{\odot}$')

        subpath = self.path[-11:]
        subpath = subpath[:6]
        plt.xlabel('M$_{\star}$ [$M_{\odot}$]')
        plt.ylabel('R$_{50}$ [Kpc]')
        plt.savefig(self.path + '/' + subpath + '_RvsMest.png')
        plt.show()

        print R50