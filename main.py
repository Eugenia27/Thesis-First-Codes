#!/usr/bin/env python
# -*- coding:utf-8 -*-
#.: MAIN CODE .

import 	numpy as np
import 	surface_brightness as sb
import 	profile as pr
import	sbrightness_profile_plot as sbp
import	intensity_profile_plot as sip
import	maps as mps
import accumulated_circular_mass as acm
import relevant_results as rr
#import	contour as cnt
#import	mass_projection as mass
import	accumulated_mass as am

_reg=input('Region: ')              #regions of clusters
_flav=input('Flav: ')               #type of
_snap=input('Snap: ')               #age of
_box=str(input('BoxSize: '))         #boxsize
_agn=raw_input('Agn(y or n): ')

_cells = input('NCells: ')

reg	=	["g0016649_G","g0052436_Me14_G","g0144846_Me14_G","g0163178_Me14_G","g0168361_Me14_G","g0272097_G",
        "g1212639_G","g1483463_G","g1574117_Me14_G","g1657050_G","g1680241_G","g1987669_G",
        "g2980844_G","g3327821_G","g3346905_G","g3888703_G","g4425770_G","g4606589_G","g4915399_G","g5265133_G",
        "g5503149_G","g5699754_G","g6287794_G","g6348555_G","g6802296_G",
        "g7263961_G","g7358274_G", "g7570066_G","g7577931_G"]

flav=	["BH2015","CSF2015"]
snap=	["041","051","071","091"]

if _agn=="y":
    path_region     =   '/home/meugenia/Documentos/masas_italia/'+reg[_reg]+'_'+flav[_flav]+'_'+snap[_snap]+'_clu0_L'+_box+'kpc'
    path_mass_data 	= 	path_region+'/'+reg[_reg]+'_'+flav[_flav]+'_091_clu0_L500kpc.dat'
    path_flux_data	=	path_region+'/map_edgeon_zlos_250__fluxinband_125.txt'
else:
    path_region     =   '/home/meugenia/Documentos/masas_italia/'+reg[_reg]+'_'+flav[_flav]+'_'+snap[_snap]+'_clu0_L'+_box+'kpc_noagn'
    path_mass_data 	= 	path_region+'/'+reg[_reg]+'_'+flav[_flav]+'_091_clu0_L500kpc_noagn.dat'
    path_flux_data	=	path_region+'/map_edgeon_zlos_250__fluxinband_125.txt'

print path_flux_data
print path_mass_data


_x,_y,_flux = np.loadtxt(path_flux_data , usecols=[0,1,3] , unpack=True)

pos_1_flux  = _x
pos_2_flux  = _y
flux        = _flux

particle_type,pos_x,pos_y,pos_z,_particle_mass = np.loadtxt(path_mass_data , skiprows=1 , usecols=[0,1,2,3,8] , unpack=True)

surfbright	=	sb.SurfaceBrightness(pos_1_flux , pos_2_flux , flux , path_region)
mu          =   surfbright.FluxToMu()

if 1==0:
    sbplots =   mps.MapAndContours(pos_1_flux , pos_2_flux , mu , path_region)
    sbplots.Map()
    sbplots.Contours()

profile	    =   pr.Profile(pos_2_flux , pos_2_flux , flux , 20 , path_region)
profile.ProfilePointsNlog()
mean_iernlog,mean_ienlog = profile.meanr,profile.meanentity
profile.ProfilePointsYlog()
mean_ierylog,mean_ieylog = profile.meanr,profile.meanentity

if 1 == 0:
	plot_ie=sip.SpecificIntensityPlot(mean_iernlog,mean_ienlog,False , path_region)
	plot_ie.Plot()
	plot_ie=sip.SpecificIntensityPlot(mean_ierylog,mean_ieylog,True , path_region)
	plot_ie.Plot()


profile	=	pr.Profile(pos_1_flux,pos_2_flux,mu,20,path_region)
profile.ProfilePointsNlog()
mean_murnlog,mean_munlog = profile.meanr,profile.meanentity
profile.ProfilePointsYlog()
mean_murylog,mean_muylog = profile.meanr,profile.meanentity


if 1 == 0:
	plot_mu=sbp.SurfaceBrightnessPlot(mean_murnlog,mean_munlog,False,path_region)
	plot_mu.Plot()
	plot_mu.Size()
	plot_mu=sbp.SurfaceBrightnessPlot(mean_murylog,mean_muylog,True,path_region)
	plot_mu.Plot()

if 1==1:
    accmasscirc = acm.AccumulatedMass(pos_1_flux , pos_2_flux , mean_munlog, mean_murnlog , particle_type , pos_x , pos_y , pos_z , _particle_mass , path_region )
    acc_masses_circ = accmasscirc.Acummulated()

    relres = rr.RelevantResults(mean_munlog,mean_murnlog, acc_masses_circ,24,path_region)
    relres.PlotMassVSRadius(_reg)

#accmasscirc.AccumulatedMassCircPlot(24)
#accmasscirc.HalfRadius()


