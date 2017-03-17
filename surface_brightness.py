import numpy as np

class SurfaceBrightness():

    def __init__(self, _x, _y, _flux, _path):
        self.x      = _x
        self.y      = _y
        self.flux   = _flux
        self.path   = _path
        self.sb     = np.zeros(len(self.x))

    def FluxToMu(self):
        self.sb = [-2.5*np.log10(fx/4.2545e10)-48.6+0.044 if fx != 0 else 50 for fx in self.flux]
        self.sb = [round(sb, 2) for sb in self.sb]
        np.savetxt(self.path + '/surface_brightness.txt', np.c_[self.x, self.y, self.sb], fmt='% 10.4f')
        return self.sb
