## This is a script to stack VANDELS spectra

The following steps are carried out to perform the stacking:
- Point to a folder containing fits files and read in the spectra
- Convert the spectra to rest frame using the redshift value given in the header file
- Create a rest-frame wavelength grid assuming a median wavelength on to which individual spectra would be resampled
- Perform a weighted average of the spectra, where the weights are based on the errors on the individual spectra
- Propagate the errors and save the stacked spectrum along with the errors!


Python packages required for essential functions:
- numpy
- astropy
- mpdaf (pip/pip3 install mpdaf)
- matplotlib (for plotting)

Additionally, to make life easier it is also useful to place the mpvandels.py file in the same folder as this notebook. This custom python package helps read in the spectra and easily convert them to rest-frame
