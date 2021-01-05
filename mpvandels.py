### Function to read in VANDELS spectra as MPDAF objects

import numpy as np 
from astropy.io import fits 
import astropy.units as u
from mpdaf.obj import Spectrum, WaveCoord

def readvandels(filename):
	### Read relevant info from VANDELS specific header entries
	hdulist = fits.open(filename)

	flux = hdulist[0].data
	header = hdulist[0].header

	crval = header['CRVAL1']
	cdelt = header['CDELT1']

	z = header['HIERARCH PND Z']
	flag = header['HIERARCH PND ZFLAGS']
	objid = header['HIERARCH PND OBJID']

	pix = np.arange(1,len(flux)+1)
	lam_i = np.zeros(len(pix))
	lam_i[0] = crval

	for j in range(len(lam_i)-1):
	    lam_i[j+1]=lam_i[j]+cdelt
	    lam_i=lam_i#/(1+float(z)) #lamda rest frame
	        
	flux = flux#*(1+float(z)) #flux rest frame
	noise = hdulist[3].data
	noise = noise#*(1+float(z)) #noise rest frame

	# Create spectrum object from VANDELS input spectrum

	wavelength = WaveCoord(crval=crval, cdelt=cdelt, cunit=u.angstrom)
	spectrum0 = Spectrum(wave=wavelength, data=flux, var=noise, unit=u.erg / u.second / u.cm**2 / u.angstrom)

	return spectrum0, float(z)


def restframespec(filename, z):
	hdulist = fits.open(filename)

	flux = hdulist[0].data
	header = hdulist[0].header

	crval = header['CRVAL1']
	cdelt = header['CDELT1']

	flag = header['HIERARCH PND ZFLAGS']
	objid = header['HIERARCH PND OBJID']

	pix = np.arange(1,len(flux)+1)
	lam_i = np.zeros(len(pix))
	lam_i[0] = crval

	for j in range(len(lam_i)-1):
	    lam_i[j+1]=lam_i[j]+cdelt
	
	lam_i=lam_i/(1+float(z)) #lamda rest frame
	        
	flux = flux*(1+float(z)) #flux rest frame
	noise = hdulist[3].data
	noise = noise*(1+float(z)) #noise rest frame

	# Create spectrum object from VANDELS input spectrum

	wavelength = WaveCoord(crval=lam_i[0], cdelt=(lam_i[-1]-lam_i[0])/len(lam_i), cunit=u.angstrom)
	restspec = Spectrum(wave=wavelength, data=flux, var=noise, unit=u.erg / u.second / u.cm**2 / u.angstrom)
	# noisespec = Spectrum(wave=wavelength, data=noise, unit=u.erg / u.second / u.cm**2 / u.angstrom)

	return restspec
