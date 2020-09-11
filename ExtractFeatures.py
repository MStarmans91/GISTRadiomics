import PREDICT
import os
import subprocess

# Configure location of input
current_path = os.path.dirname(os.path.abspath(__file__))
image = os.path.join(current_path,
                     'ExampleData', 'ExampleImage.nii.gz')
segmentation = os.path.join(current_path,
                            'ExampleData', 'ExampleSegmentation.nii.gz')
metadata = os.path.join(current_path,
                        'ExampleData', 'ExampleDCM.dcm')
config_predict = os.path.join(current_path,
                              'ExampleData', 'config.ini')
config_pyradiomics = os.path.join(current_path,
                                  'ExampleData', 'config_pyradiomics.yaml')

# Configure location of output
output_predict = os.path.join(current_path,
                              'ExampleData',
                              'ExampleFeaturesPREDICT.hdf5')
output_pyradiomics = os.path.join(current_path,
                                  'ExampleData',
                                  'ExampleFeaturesPyRadiomics.csv')

# Extract PREDICT features
PREDICT.CalcFeatures.CalcFeatures(image=image, segmentation=segmentation,
                                  parameters=config_predict,
                                  metadata_file=metadata,
                                  output=output_predict)

# Extract pyradiomics features
cmd = [
    'pyradiomics',
    '"' + image + '"',
    '"' + segmentation + '"',
    '--param', '"' + config_pyradiomics + '"',
    '--format', 'csv',
    '--out', '"' + output_pyradiomics + '"'
    ]

print(' '.join(cmd))
output = subprocess.check_output(cmd)
