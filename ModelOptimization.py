import WORC
import os
import glob
from classes import switch


def editconfig(config):
    """Edit the WORC default configuration to the GIST config."""
    # Use Segmentix to fill holes if present in the segmentation
    config['General']['Segmentix'] = 'True'

    # Some specific configuration alterations
    config['Preprocessing']['Normalize'] = 'False'  # No Normalization for CT

    config['ImageFeatures']['image_type'] = 'CT'
    config['ImageFeatures']['vessel_radius'] = '0'  # tumors can be really small

    # NOTE: Change this label if you want to predict something different, e.g. KIT_Exon_11.
    # This should correspond to the names in the label_file, see below.
    config['Labels']['label_names'] = 'GIST'
    config['Labels']['modus'] = 'singlelabel'

    # NOTE: Since we now only use 10 "patients" in this example, we do not use resampling.
    # Do not do this for the full experiment.
    config['Resampling']['Use'] = '0.0'

    return config


# Inputs
name = 'WORC_GIST_DD'
current_path = os.path.dirname(os.path.abspath(__file__))
label_file = os.path.join(current_path, 'ExampleData', 'pinfo_GIST.csv')
semantics_file = os.path.join(current_path, 'ExampleData', 'sem_GIST.csv')
config = os.path.join(current_path, 'ExampleData', 'config.ini')

# Altough you can also the features, we will supply the raw image
images = glob.glob(os.path.join(current_path, 'ExampleData', 'ExampleImage*.nii.gz'))
images.sort()

segmentations = glob.glob(os.path.join(current_path, 'ExampleData', 'ExampleSegmentation*.nii.gz'))
segmentations.sort()

metadatas = glob.glob(os.path.join(current_path, 'ExampleData', 'ExampleDCM*.dcm'))
metadatas.sort()

# As we only have a single patient/object, hence we will repeat it to mimick
# having multiple. We do this in a dictionary, in which the keys
# correspond to the "patient" names also used in the label and semantics files
patient_names = ['GISTRadiomics-' + str(i).zfill(3) for i in range(0, 10)]
images = {k: images[0] for k in patient_names}
segmentations = {k: segmentations[0] for k in patient_names}
metadatas = {k: metadatas[0] for k in patient_names}

# Create the WORC network
network = WORC.WORC(name)
network.labels_train.append(label_file)

# Instead of supplying the .ini file to the network, we will create
# the config object for you directly from WORC,
# so you can interact with it if you want.
# Altough it is a configparser object, it works similar as a dictionary
config = network.defaultconfig()

# The default config from the WORC 3.4.0 version we used, was a stripped
# version in order to get a quick result. The actual default used for normal
# experiments is created through the editconfig function.
config = editconfig(config)

# Specific additions for each model discussed in the paper
option = 'model_3_imaging'
for case in switch(option):
    if case('model_1_volume'):
        # NOTE: You will need to manually strip the feature files to only keep
        # the feature named sf_volume_2D and supply these to the network
        # instead of the images
        feature_files = glob.glob(os.path.join(current_path, 'ExampleData', 'GISTRadiomics*_volume.hdf5'))
        feature_files.sort()

        # Append the sources to be used
        network.features_train.append(feature_files)
        network.configs.append(config)

        break

    if case('model_2_agesex'):
        # Use only the semantic featues = age and gender
        config['SelectFeatGroup']['shape_features'] = 'False'
        config['SelectFeatGroup']['histogram_features'] = 'False'
        config['SelectFeatGroup']['orientation_features'] = 'False'
        config['SelectFeatGroup']['texture_Gabor_features'] = 'False'
        config['SelectFeatGroup']['texture_GLCM_features'] = 'False'
        config['SelectFeatGroup']['texture_GLCMMS_features'] = 'False'
        config['SelectFeatGroup']['texture_GLRLM_features'] = 'False'
        config['SelectFeatGroup']['texture_GLSZM_features'] = 'False'
        config['SelectFeatGroup']['texture_NGTDM_features'] = 'False'
        config['SelectFeatGroup']['texture_LBP_features'] = 'False'
        config['SelectFeatGroup']['patient_features'] = 'False'
        config['SelectFeatGroup']['semantic_features'] = 'True'
        config['SelectFeatGroup']['coliage_features'] = 'False'
        config['SelectFeatGroup']['vessel_features'] = 'False'
        config['SelectFeatGroup']['phase_features'] = 'False'
        config['SelectFeatGroup']['log_features'] = 'False'

        # Append the sources to be used
        network.images_train.append(images)
        network.segmentations_train.append(segmentations)
        network.metadata_train.append(metadatas)
        network.semantics_train.append(semantics_file)
        network.configs.append(config)

        break

    if case('model_3_imaging'):
        # Set the non-imaging feature groups to False so they are not used
        config['SelectFeatGroup']['semantic_features'] = 'False'
        config['SelectFeatGroup']['patient_features'] = 'False'

        # Append the sources to be used
        network.images_train.append(images)
        network.segmentations_train.append(segmentations)
        network.metadata_train.append(metadatas)
        network.semantics_train.append(semantics_file)
        network.configs.append(config)

        break

    if case('model_4_imagingagesexloc'):
        # Append the sources to be used
        network.images_train.append(images)
        network.segmentations_train.append(segmentations)
        network.metadata_train.append(metadatas)
        network.semantics_train.append(semantics_file)
        network.configs.append(config)

        break


# Build, set, and execture the network
network.build()
network.set()
network.execute()

# NOTE: if you want extensive evaluation including ROC curves, statistical
# testing of features, add ``network.add_evaluation('GIST')'' after
# network.build().
