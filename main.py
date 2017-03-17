#!/usr/bin/env python
# -*- coding:utf-8 -*-
#.: MAIN CODE .

import 	numpy as np
import 	surface_brightness as sb

#import 	profile as pr
#import	mu_profile_plot as muplot
#import	ie_profile_plot as ieplot
import	maps as mps
#import	contour as cnt
#import	mass_projection as mass
#import	accumulated_mass as accmass

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


_x,_y,_flux = np.loadtxt(path_flux_data, usecols=[0,1,3], unpack=True)
#print _x,_y
pos_1_flux = _x
pos_2_flux = _y
flux = _flux

particle_type,pos_x,pos_y,pos_z,_particle_mass = np.loadtxt(path_mass_data, skiprows=1, usecols=[0,1,2,3,8], unpack=True)

surfbright	=	sb.SurfaceBrightness(pos_1_flux,pos_2_flux,flux,path_region)
mu          =   surfbright.FluxToMu()

if 1==1:
    sbplots=mps.MapAndContours(pos_1_flux,pos_2_flux,mu,path_region)
    sbplots.Map()
    #sbplots.Contours()

#profile	=  pr._Profile(x,y,flux,20,path_region)
#mean_r,mean_ie,mean_logr,mean_ie_logr	=  profile._ProfilePoints()

#print '***********************************************************************************************'
#graficar	=	input('---------Make Specific Intensity profiles? (type 1 if YES or 0 if NO)--------- ')
#if graficar == 1:
#	plot_ie=ieplot._SIPlot(mean_r,mean_ie,False)
#	plot_ie._Plot()
#	plot_ie=ieplot._SIPlot(mean_logr,mean_ie_logr,True)
#	plot_ie._Plot()
#	print 'Really Good! ;)'


#print '***********************************************************************************************'
#profile	=	pr._Profile(x,y,_mu,20,path_region)
#mean_r,mean_mu,mean_logr,mean_mu_logr	=	profile._ProfilePoints()

#graficar	=	input('--------Make Surface Brightness profiles? (type 1 if YES or 0 if NO)--------- ')
#if graficar == 1:
#	plot_mu=muplot._SBPlot(mean_r,mean_mu,False,path_region)
#	plot_mu._Plot()
#	plot_mu._Size()
#	plot_mu=muplot._SBPlot(mean_logr,mean_mu_logr,True,path_region)
#	plot_mu._Plot()
#	print 'Ok!!!'

#mass_pr = mass._MassProjection(type_p,xx,yy,xx,mass_p,int(box),cells)
#x_projection = np.zeros((cells,cells))
#x_projection, y_projection, z_projection = mass_pr._MassMatrices()
#for i in range(cells):
#	for j in range(cells):
#		if x_projection[i][j] != 0. or y_projection[i][j] != 0. or z_projection[i][j] != 0. :
#			print ('%15.4e %15.4e %15.4e' %(x_projection[i][j] , y_projection[i][j] ,z_projection[i][j]))

#x_projection =	np.asarray(x_projection)

#print '***********************************************************************************************'
#graficar	=	input('--------Make Mass Projection contours plots? (type 1 if YES or 0 if NO)--------- ')
#if graficar == 1:
#	maps_mass=mps._MapsPlot(x,y,x_projection,1)
#	maps_mass._Plot()
#	cnts_mass=cnt._ContoursPlot(x,y,x_projection,1)
#	cnts_mass._Plot()
#	print 'WWWoooWWW!!!'



#print '***********************************************************************************************'
#acc	=	accmass._AccumulatedMass(x,y,_mu,path_region,path_mass_data)
#graficar	=	input('-------- Calcular Masas Acumuladas? --------- ')

#if graficar == 1:
#    semi,masas,dimens = acc._Acumuladas()

#acc._MassPlot()
#acc._R50()


#print '***********************************************************************************************'
#print 'Come Back For More!!'
