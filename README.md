# GISTRadiomics
[![DOI](https://zenodo.org/badge/229019002.svg)](https://zenodo.org/badge/latestdoi/229019002)

Scripts to compute the features and fit radiomics models as used in the paper
"Differential diagnosis and molecular stratification of gastrointestinal stromal
tumors on CT images using a radiomics approach." M. P. A. Starmans, M. J. M. Timbergen et al.

## Installation
For both the feature extraction and model optimization, WORC, version 3.3.3,
is required:

    pip install "WORC==3.3.3"

## Usage: Feature Extraction
The ExtractFeatures.py script can be used to extract all features. We provided
you with the exact same configuration file that was used in the study. The
script can be easily modified to use your own data instead of the
provided example data and requires:

1. An image in ITK Image format, e.g. .nii, .nii.gz, .tiff, .nrrd, .raw
2. A segmentation in ITK Image format.
3. Optionally, metadata in DCM format

Extracting the features from the example data should take less than 10 seconds.
Using a larger image and/or mask may result in a longer computation time.

## Usage: Model Optimization
The ModelOptimization.py script can be used for the model optimization. Again,
we provided you with the exact same configuration file that was used in the study.
The script can be easily modified to use your own data instead of the
provided example data and requires: see for more details the script itself.

Note that the script performs a dummy experiment: it supplies 10x the example
features to WORC, which will result in non-separable dataset, and thus no
sensible model. Usage of your own data is therefore highly recommended.

## Known Issues
For some of the known issues, please visit the WORC FAQ:
https://worc.readthedocs.io/en/latest/static/faq.html.

## P-values of statistically significant features
In the "StatisticalTestFeatures_significant_bonferonni.xlsx" file, the p-values
of the Mann-Whitney U / Chi-square test after Bonferonni multiple testing correction are listed.
Only those features with a p-value < 0.05 after correction are included, thus those
that have a statistically significant different distribution in GIST vs. non-GIST
patients.

The labels contain:
- The feature group:
    - semf: semantic feature, which are the non-computational features
    - tf: texture feature
    - hf: histogram feature, corresponding to the intensity histogram
    - vf: vessel feature, obtained after applying a vessel filter to the image
- For the texture features, the subtype, see Supplementary Materials S1 of the manuscript.
- The name of the feature within the group and/or subtype.
- Optionally, the parameters used to obtain that feature.

For example, "tf_Gabor_0.05A0.0kurt_Features_0" is a texture feature,
subtype Gabor, i.e. computed after applying a Gabor filter using parameters
0.05 for the frequency and 0.0 for the angle, containing the kurtosis.

For more details on each feature, see the [WORC Documentation](https://worc.readthedocs.io/en/latest/static/features.html).
