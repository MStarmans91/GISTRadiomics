[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.3839322.svg)](https://doi.org/10.5281/zenodo.3839322)

# GISTRadiomics
Scripts to compute the features and fit radiomics models as used in the following paper:

``M. P. A. Starmans, M. J. M. Timbergen, M. Vos, M. Renckens, D. J. Grünhagen,
G. J. L. H. van Leenders, R. S. Dwarkasing, F. E. J. A. Willemssen, W. J. Niessen,
C. Verhoef, S. Sleijfer, J. J. Visser, and S. Klein, “Differential Diagnosis and Molecular Stratification of Gastrointestinal Stromal Tumors on CT Images Using a Radiomics Approach,” J Digit Imaging 35, 127–136 (2022). https://doi.org/10.1007/s10278-022-00590-2``

Before using the code in this repository, we advice you to get
familiar with the WORC package through the WORC tutorial:
https://github.com/MStarmans91/WORCTutorial.

## License
This package is covered by the open source [APACHE 2.0 License](APACHE-LICENSE-2.0).

When using this code, please cite this repository and the corresponding paper
as following:

``M.P.A Starmans. GISTRadiomics. Zenodo (2022). Available from: https://github.com/MStarmans91/GISTRadiomics, DOI: https://doi.org/10.5281/zenodo.3839322.``

``M. P. A. Starmans, M. J. M. Timbergen, M. Vos, M. Renckens, D. J. Grünhagen,
G. J. L. H. van Leenders, R. S. Dwarkasing, F. E. J. A. Willemssen, W. J. Niessen,
C. Verhoef, S. Sleijfer, J. J. Visser, and S. Klein, “Differential Diagnosis and Molecular Stratification of Gastrointestinal Stromal Tumors on CT Images Using a Radiomics Approach,” J Digit Imaging 35, 127–136 (2022). https://doi.org/10.1007/s10278-022-00590-2``


## Installation
For both the feature extraction and model optimization, WORC, version 3.4.0,
is required:

    pip install "WORC==3.4.0"

While newer versions are supported, for the analysis presented in the paper,
we used PREDICT version 3.1.13 and PyRadiomics version 3.0.1, see the requirements.txt file.

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

## Usage: Dataset
The GIST dataset as used in the paper was publicly released as part of the following paper:

``Starmans, M. P. A. et al. (2021). The WORC* database: MRI and CT scans, segmentations, and clinical labels for 932 patients from six radiomics studies, Submitted, Preprint available at https://doi.org/10.1101/2021.08.19.21262238.``

The data can be found at https://xnat.bmia.nl/data/projects/worc; scripts to download the data can be found at https://github.com/MStarmans91/WORCDatabase, including a script to reproduce the experiment for the imaging only radiomics model of this GIST study.

## Known Issues
For some of the known issues, please visit the WORC FAQ:
https://worc.readthedocs.io/en/latest/static/faq.html.

## P-values of statistically significant features
In the FeatureTests folder, outputs of two statistical tests are provided.

First,
in the "StatisticalTestFeatures_significant_bonferonni.xlsx" file, the p-values
of the Mann-Whitney U / Chi-square test after Bonferonni multiple testing correction are listed.
Only those features with a p-value <= 0.05 after correction are included, thus those
that have a statistically significant different distribution in GIST vs. non-GIST
patients.

Second,
in the "ICCvalues.xlsx", the intra-class correlation coefficient (ICC)
of all features are listed. These were calculated on a subset of 30 GISTs
which were segmented by two observers

The labels contain:
- The feature group:
    - semf: semantic feature, which are the non-computational features
    - tf: texture feature. For the texture features, the subtype, see Supplementary Material 1 of the manuscript. Some texture features have separate groups as these are less common, but can be regarded as texture features nonetheless:
      - vf: vessel feature, obtained after applying a vessel filter to the image
      - logf: obtained after applying a Laplacian of Gaussian filter to the image
      - phasef: local phase features, obtained after obtaining the local phase of the image
    - hf: histogram feature, corresponding to the intensity histogram
- The name of the feature within the group and/or subtype.
- Optionally, the parameters used to obtain that feature.

For example, "tf_Gabor_kurt_F0.2_A0.0" is a texture feature,
subtype Gabor, i.e., computed after applying a Gabor filter using parameters
0.2 for the frequency and 0.0 for the angle, containing the kurtosis.

For more details on each feature, see the [WORC Documentation](https://worc.readthedocs.io/en/latest/static/features.html).

## Hyperparameters of final models
For the imaging only model as presented in the paper, in the SelectedWorkflows
folder, the Hyperparameters_all_0.csv file specifies the hyperparameters of the top 100 performing workflows as included in the ensemble for each of the 100 cross-validation iterations.

The first columns state additional information:
- The train-test cross-validation iteration
- The rank of the workflow in that cross-validation iteration
- The mean scores (weighted F1-score in this case) on the training and validation set
  within the train-validation cross-validation
- The mean fit time
