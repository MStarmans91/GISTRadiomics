import PREDICT

# Configure location of input
image = 'ExampleImage.nii.gz'
segmentation = 'ExampleSegmenation.nii.gz'
metadata = 'ExampleDCM.dcm'
config = 'config_features.ini'

# Configure location of output
output = 'ExampleFeatures.hdf5'


PREDICT.CalcFeatures.CalcFeatures(image=image, segmentation=segmentation,
                                  parameters=config, metadata_file=metadata,
                                  output=output)
