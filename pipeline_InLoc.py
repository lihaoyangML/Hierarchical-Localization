%load_ext autoreload
%autoreload 2

from pathlib import Path
from pprint import pformat

from hloc import extract_features, match_features, localize_inloc, visualization

dataset = Path('datasets/inloc/')  # change this if your dataset is somewhere else

pairs = Path('pairs/inloc/')
loc_pairs = pairs / 'pairs-query-netvlad40.txt'  # top 40 retrieved by NetVLAD

outputs = Path('outputs/inloc/')  # where everything will be saved
results = outputs / 'InLoc_hloc_superpoint+superglue_netvlad40.txt'  # the result file

# list the standard configurations available
print(f'Configs for feature extractors:\n{pformat(extract_features.confs)}')
print(f'Configs for feature matchers:\n{pformat(match_features.confs)}')

# pick one of the configurations for extraction and matching
# you can also simply write your own here!
feature_conf = extract_features.confs['superpoint_inloc']
matcher_conf = match_features.confs['superglue']

feature_path = extract_features.main(feature_conf, dataset, outputs)

match_path = match_features.main(matcher_conf, loc_pairs, feature_conf['output'], outputs)

localize_inloc.main(
    dataset, loc_pairs, feature_path, match_path, results,
    skip_matches=20)  # skip database images with too few matches