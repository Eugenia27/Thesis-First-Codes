import numpy as np
import math as mt

class Profile():

    def __init__(self, _x, _y, _entity, _nbin, _path_region):
        self.x          = _x
        self.y          = _y
        self.entity     = _entity
        self.nbin       = _nbin
        self.path       = _path_region
        self.meanr      = np.zeros(_nbin)
        self.meanentity = np.zeros(_nbin)
        self.type       = ''

    def _ProyDistance(self,x,y):
        distance = mt.sqrt(x*x+y*y)
        return distance


    def _MeanValues(self, path, _min, _step, n_elements, mean_r, mean_entity):
        self.meanr      = np.zeros(self.nbin)
        self.meanentity = np.zeros(self.nbin)
        for i in range(self.nbin):
            if n_elements[i] > 0:
                self.meanr[i] = _min + (2 * i + 1) * _step / 2.
                self.meanentity[i] = mean_entity[i] / n_elements[i]

        np.savetxt(path, np.c_[self.meanr, self.meanentity], fmt='%10.4g %10.4g')


    def _CheckBinnes(self, _elements,_log):
        withlog = _log
        boolean = True
        for i in _elements:
            if i == 0:
                self.nbin = self.nbin -1
                boolean = False
                return boolean
                break
        return boolean


    def ProfilePointsNlog(self,_type):
        nbin = self.nbin
        value = self.entity
        self.type = _type

        mean_entitynlog = np.zeros(nbin)
        n_elementsnlog  = np.zeros(nbin)
        mean_rnlog      = np.zeros(nbin)

        rnlog = [self._ProyDistance(x,y) for x, y in zip(self.x, self.y)]
        [maxnlog, minnlog] = [np.amax(rnlog), 0]#np.amin(rnlog)]
        stepnlog = (maxnlog - minnlog) / float(nbin)

        for rn, val in zip(rnlog, value):
            if val > 0. and rn < maxnlog:
                binnlog = int(mt.floor((rn - minnlog) / stepnlog))
                n_elementsnlog[binnlog] += 1
                mean_entitynlog[binnlog] = mean_entitynlog[binnlog] + val


        boolean = self._CheckBinnes(n_elementsnlog, False)
        if boolean == False:
            self.ProfilePointsNlog(self.type)
        else:
            if self.type == 'mu':
                #self._MeanValues(self.path + '/mean_munlog.txt', minnlog, stepnlog, n_elementsnlog, mean_rnlog , mean_entitynlog)
                self._MeanValues(self.path + '/mean_munlog.txt', 0, stepnlog, n_elementsnlog, mean_rnlog , mean_entitynlog)
            else:
                #self._MeanValues(self.path + '/mean_ienlog.txt', minnlog, stepnlog, n_elementsnlog, mean_rnlog , mean_entitynlog)
                self._MeanValues(self.path + '/mean_munlog.txt', 0, stepnlog, n_elementsnlog, mean_rnlog,  mean_entitynlog)
            return True


    def ProfilePointsYlog(self, _type):
        nbin = self.nbin
        value = self.entity
        self.type = _type

        mean_entityylog = np.zeros(nbin)
        n_elementsylog  = np.zeros(nbin)
        mean_rylog      = np.zeros(nbin)

        r = [self._ProyDistance(x,y) for x, y in zip(self.x, self.y)]
        rylog = [np.log10(rr) for rr in r]
        [maxylog, minylog] = [np.amax(rylog), np.amin(rylog)]
        stepylog = (maxylog - minylog) / float(nbin)

        for ry, val in zip(rylog, value):
            if val > 0. and ry < maxylog:
                binylog = int(mt.floor((ry - minylog) / stepylog))
                n_elementsylog[binylog] += 1
                mean_entityylog[binylog] = mean_entityylog[binylog] + val

        boolean = self._CheckBinnes(n_elementsylog, True)
        if boolean == False:
            if self.nbin < 5:
                return False
            self.ProfilePointsYlog(self.type)
        else:
            if self.type == 'mu':
                self._MeanValues(self.path + '/mean_muylog.txt', minylog, stepylog, n_elementsylog, mean_rylog , mean_entityylog)
            else:
                self._MeanValues(self.path + '/mean_ieylog.txt', minylog, stepylog, n_elementsylog, mean_rylog , mean_entityylog)
            return True
