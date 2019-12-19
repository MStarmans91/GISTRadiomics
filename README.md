# GISTRadiomics
Scripts to compute the features and fit radiomics models as used in the paper "Differential diagnosis and molecular stratification of gastrointestinal stromal tumors on CT images using a radiomics approach." M. P. A. Starmans, M. J. M. Timbergen  et al. 2019.

## Installation
For the feature extraction, only the PREDICT package, version 2.1.3,
and the subsequent dependencies are required, which can be installed through pip:

    pip install "PREDICT==2.1.3"

For the model optimization, additionally WORC, version 2.1.3, is required:

    pip install "WORC==2.1.3"

When training or testing model 5 - 7, elastix is required to align the T2 (FS or non-FS)
to the T1. Make sure there elastix is installed on your PC and can be called on
the command line using the "elastix" command. See here for the installation
instructions: http://elastix.isi.uu.nl/

## Usage
The ExtractFeatures.py script can be used to extract all features. We provided
you with the exact same configuration file that was used in the study. The
script can be easily modified to use your own data instead of the
provided example data and requires:

1. An image in ITK Image format, e.g. .nii, .nii.gz, .tiff, .nrrd, .raw
2. A segmentation in ITK Image format.
3. Optionally, metadata in DCM format

Extracting the features from the example data should take less than 10 seconds.
Using a larger image and/or mask may result in a longer computation time.

Documentation for the model optimization is provided in the respective script.

## Known Issues

### Pyradiomics
The PyRadiomics package we use requires numpy in the installation, hence
you may need to install numpy manually beforehand:

    pip install "numpy==1.6.4"

From version 2.2.0 and above, PyRadiomics removed a function and might throw
this error:

'''AttributeError: 'module' object has no attribute "RadiomicsFeaturesExtractor"'''

This can be overcome by downgrading to version 2.1.2:

    pip install "pyradiomics==2.1.2"

### Missingpy
Missingpy version 0.2.0 may throw an ascii error: in that case, manually
remove and reinstall the package:

    pip uninstall missingpy
    pip install "missingpy==0.2.0"
