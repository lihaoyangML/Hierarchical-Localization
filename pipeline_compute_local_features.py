%load_ext autoreload
%autoreload 2

from pathlib import Path

from hloc import extract_features, match_features, reconstruction, visualization

dataset = Path('../../gangnam/GangnamStation/B2/release/mapping/sensors/records_data/2019-12-03_10-54-54/')
images = dataset / 'images'

outputs = Path('../../gangnam/sfm/')
sfm_pairs = outputs / 'pairs-exhaustive.txt'  # exhaustive matching
sfm_dir = outputs / 'sfm_superpoint+superglue'

feature_conf = extract_features.confs['superpoint_aachen']
matcher_conf = match_features.confs['superglue']

feature_path = extract_features.main(feature_conf, images, outputs)