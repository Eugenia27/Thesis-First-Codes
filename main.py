#!/usr/bin/env python
# -*- coding:utf-8 -*-
#.: MAIN CODE .

import 	numpy as np
import 	surface_brightness as sb
import 	profile as pr
import	sbrightness_profile_plot as sbp
import	intensity_profile_plot as sip
import	maps as mps
import  accumulated_circular_mass as acm
import  relevant_results as rr
#import	contour as cnt
#import	mass_projection as mass
import	accumulated_mass as am

_reg        = input('Region: ')
_flav       = 1                                 #input('Flav: ')
_snap       = 2 #input('Snap: ')
_box        = 500                               #str(input('BoxSize: '))
_progenitor = 0 #input('Bias(0),Direct(1): ')
_cells      = 250                               #input('NCells: ')
_mulim      = 24                                #input('Mu limit: ')
_dust       = 0
_mask       = 1
resolution  = _box/_cells

reg = ["NONE","D1","D2","D3","D4","D5","D6","D7","D8","D9","D10","D11","D12","D13","D14",
       "D15","D16","D17","D18","D19","D20","D21","D22","D23","D24","D25","D26","D27","D28","D29"]

flav       = ["BH2015","CSF2015"]
snap       = ["032","041","091"]
progenitor = ["BiasedProg","DirProg"]
prog_type  = ["BP","DP"]
dust       = ["nodust","dust"]
mask       = ["nomask","mask"]

path_dir       = '/home/meugenia/0/resultados/'+flav[_flav]+'/'+dust[_dust]+'_'+mask[_mask]+'/'
path_region    = '/home/meugenia/0/resultados/'+flav[_flav]+'/'+dust[_dust]+'_'+mask[_mask]+'/'+reg[_reg]+'/'+snap[_snap]+'/'
if _progenitor==1:
    path_region = '/home/meugenia/0/resultados/'+flav[_flav]+'/'+dust[_dust]+'_'+mask[_mask]+'/Directs/' + reg[_reg] + '/' + snap[_snap] + '/'
pattern        = flav[_flav]+'_'+reg[_reg]+'_'+snap[_snap]+'_'+prog_type[_progenitor]+dust[_dust]
path_mass_data = path_region+pattern+'.dat'
path_flux_data = path_region+'map_edgeon_zlos_250__fluxinband_125_'+pattern+'.txt'

print path_flux_data
print path_mass_data

_x,_y,_flux = np.loadtxt(path_flux_data , usecols=[0,1,3] , unpack=True)

pos_1_flux = _x
pos_2_flux = _y
flux       = _flux

particle_type,pos_x,pos_y,pos_z,_particle_mass = np.loadtxt(path_mass_data , skiprows=1 , usecols=[0,1,2,3,8] , unpack=True)

surfbright	= sb.SurfaceBrightness(pos_1_flux , pos_2_flux , flux , path_region)
mu          = surfbright.FluxToMu()

if 1==1:
    sbplots = mps.MapAndContours(pos_1_flux , pos_2_flux , mu , path_region)
    sbplots.Map()
    sbplots.Contours()

#rmax_flux = np.sqrt((np.max(pos_1_flux))**2 + (np.max(pos_2_flux))**2)
#bines     = int(rmax_flux/resolution)

#profile	    =   pr.Profile(pos_2_flux , pos_2_flux , flux , bines , path_region)
#profile.ProfilePointsNlog('si')
#mean_iernlog,mean_ienlog = profile.meanr,profile.meanentity
#profile.ProfilePointsYlog('si')
#mean_ierylog,mean_ieylog = profile.meanr,profile.meanentity

#if 1 == 0:
#	plot_ie=sip.SpecificIntensityPlot(mean_iernlog,mean_ienlog,False , path_region)
#	plot_ie.Plot()
#	plot_ie=sip.SpecificIntensityPlot(mean_ierylog,mean_ieylog,True , path_region)
#	plot_ie.Plot()


"""Defino el numeros de bines a usar en base a un multiplo de la resolucion, distancias sin logaritomo"""
rmax_flux_nl = np.sqrt((np.max(pos_1_flux))**2 + (np.max(pos_2_flux))**2)
bines_nl     = int(rmax_flux_nl/resolution)
profile_nl	 = pr.Profile(pos_1_flux , pos_2_flux , mu , bines_nl , path_region)
profile_nl.ProfilePointsNlog('mu')
mean_murnlog,mean_munlog = profile_nl.meanr,profile_nl.meanentity

"""Defino el numeros de bines a usar en base a un multiplo de la resolucion, distancias con logaritomo"""
rmax_flux_yl = np.sqrt((np.log10(np.max(pos_1_flux)))**2 + (np.log10(np.max(pos_2_flux)))**2)
bines_yl     = int(rmax_flux_yl/np.log10(resolution))
profile_yl	 = pr.Profile(pos_1_flux , pos_2_flux , mu , bines_yl , path_region)
profile_yl.ProfilePointsYlog('mu')
mean_murylog,mean_muylog = profile_yl.meanr,profile_yl.meanentity

if 1 == 1:
	plot_mu = sbp.SurfaceBrightnessPlot(mean_murnlog,mean_munlog,False,path_region)
	plot_mu.Plot()
	plot_mu = sbp.SurfaceBrightnessPlot(mean_murylog,mean_muylog,True,path_region)
	plot_mu.Plot()

if 1==1:
    accmasscirc     = acm.AccumulatedMass(pos_1_flux , pos_2_flux , mean_munlog, mean_murnlog , particle_type , pos_x , pos_y , pos_z , _particle_mass , path_region )
    acc_masses_circ = accmasscirc.Acummulated()

    relres = rr.RelevantResults(mean_munlog,mean_murnlog, acc_masses_circ,_mulim,path_region)
    relres.PlotMassVSRadius(_reg,snap[_snap],prog_type[_progenitor],path_dir)

#accmasscirc.AccumulatedMassCircPlot(24)
#accmasscirc.HalfRadius()


