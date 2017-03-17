import numpy as np
import math as mt

class _Profile():

    def __init__(self, _x, _y, _entity, _nbin, _path_region):
        self.x = _x
        self.y = _y
        self.entity = _entity
        self.nbin = _nbin
        self.path = _path_region

    def _ProyDistance(self,x,y):
        distance = mt.sqrt(x*x+y*y)
        return distance

    def _ProfilePoints(self):
        nbin = self.nbin

        rnlog = [self._ProyDistance(x,y) for x, y in zip(self.x, self.y)]
        rylog = [np.log10(r) for r in rnlog]
        value = self.entity

        [maxnlog, minnlog] = [np.amax(rnlog), np.amin(rnlog)]
        [maxylog, minylog] = [np.amax(rylog), np.amin(rylog)]
        stepnlog = (maxnlog - minnlog) / float(nbin)
        stepylog = (maxylog - minylog) / float(nbin)

        #print min_, max_, step

        mean_entity_nlog, mean_entity_wlog = np.zeros(nbin), np.zeros(nbin)
        n_elements_nlog, n_elements_wlog = np.zeros(nbin), np.zeros(nbin)
        mean_r_nlog, mean_r_wlog = np.zeros(nbin), np.zeros(nbin)

        for r_, r_wlog_, value_ in zip(r, r_wlog, value):
            if value_ > 0. and (r_ != max_ or r_wlog_ != max_wlog):
                bin_ = int(mt.floor((r_ - min_) / step))
                n_elements_nlog[bin_] += 1
                mean_entity_nlog[bin_] = mean_entity_nlog[bin_] + value_
                bin_wlog = int(mt.floor((r_wlog_ - min_wlog) / step_wlog))
                n_elements_wlog[bin_wlog] += 1
                mean_entity_wlog[bin_wlog] = mean_entity_wlog[bin_wlog] + value_
                # print value_, "      ",bin_,"    ",n_elements_nlog[bin_]

        [mean_r_nlog, mean_entity_nlog] = self._ValoresMedios(self.path + '/mean_mu_nlog.txt', min_, step, n_elements_nlog, mean_r_nlog, mean_entity_nlog)
        [mean_r_wlog, mean_entity_wlog] = self._ValoresMedios(self.path + '/mean_mu_wlog.txt', min_wlog, step_wlog, n_elements_wlog, mean_r_wlog, mean_entity_wlog)
        ellip = np.zeros(len(mean_r_nlog))
        pa = np.zeros(len(mean_r_nlog))
        np.savetxt(self.path + '/elipses.txt', np.c_[mean_r_nlog, ellip, pa], fmt='%10.4g %10.4g %10.4g')
        return mean_r_nlog, mean_entity_nlog, mean_r_wlog, mean_entity_wlog

    def _ValoresMedios(self, path, _min, _step, n_elements, mean_r, mean_entity):
        for i in range(self.binn):
            if n_elements[i] != 0:
                mean_r[i] = _min + (2 * i + 1) * _step / 2.
                mean_entity[i] = mean_entity[i] / n_elements[i]

        np.savetxt(path, np.c_[mean_r, mean_entity], fmt='%10.4g %10.4g')

        return [mean_r, mean_entity]