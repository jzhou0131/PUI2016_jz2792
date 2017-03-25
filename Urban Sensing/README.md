# Urban Sensing: Spectrometers

## Assignment

### Manual Calibration of CFL Spectra
Use the foldable spectrometer to capture a sepctra from a CFL bulb.  Using python, calibrate the image.  Think about the calibration discussion in class (i.e. one point, two point, multi-point techniques) and use the Spectral Workbench process as a methodological guide.

Start the process by determining the calibration points.  Spectral Workbench calibration is based on two peaks - a blue peak at 435.8nm and 546.1nm respectively.  You should try and identify other peaks in order to enhance your calibration accuracy.

An example spectrum image can be found in the ```data``` folder.
    
### Capture Urban Spectra
New York City is full of lights!  Use the spectrometer to capture as many diverse lighting types as you can find.  Try and analyze  the capture spectra to identify the lighting type.  There are several challenges here:

1. If you're using the foldable spectrometer, calibration will be extremely difficult.
2. Does the foldable spectrometer have the resolution and range to produce a usable spectrum? 
3. If you're able to capture a calibrated light source (other than a CFL bulb), how does one determine elements creating the emission?  Use the resources below to examine known spectra and compare those known to the spectra you've captured.  How well do multiple spectra compare?  Can you quantitatively measure this?

The data folder has an example spectra from something other than a CFL bulb.  The spectra was calibrated through Spectral Workbench.  Are you able to identify the type of light generating the spectra?  I've included 5 possible spectra in ```known_spectra_peaks``` folder.

## Resources

- [Known spectra](http://astro.u-strasbg.fr/~koppen/discharge/): This is a collection of the basic elements and their spectra.  There is .jpg image (uncalibrated) as well as text a text document with the identifying peaks. 
- [Fluorescent lighting spectra (wikipedia)](https://en.wikipedia.org/wiki/File:Fluorescent_lighting_spectrum_peaks_labelled.gif)
- [Spectral Workbench implementation](https://spectralworkbench.org/macro/nathanathan/Fastie-emission-absorption-curve): implemented in javascript.