# ActSTD

The official implementation of "Activity Trajectory Generation via Modeling Spatiotemporal Dynamics" (KDD '22)

## Dependency
Check python packages listed in the requirements.txt file.

## lack
args.run_name
args.data
import GaussianMixtureSpatialModel, IndependentCN
from Evaluation import *
from viz_dataset import load_data, MAPS
from models.temporal import HomogeneousPoissonPointProcess, HawkesPointProcess, SelfCorrectingPointProcess