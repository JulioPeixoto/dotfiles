import warnings
from collections import defaultdict as defaultdict
from numbers import Integral as Integral, Real as Real
from typing import Any, ClassVar
from typing_extensions import Self

import numpy as np
from numpy import ndarray
from numpy.random import RandomState

from .._config import config_context as config_context
from .._typing import Float, Int, MatrixLike
from ..base import BaseEstimator, ClusterMixin
from ..metrics.pairwise import pairwise_distances_argmin as pairwise_distances_argmin
from ..neighbors import NearestNeighbors as NearestNeighbors
from ..utils import check_array as check_array, check_random_state as check_random_state, gen_batches as gen_batches
from ..utils._param_validation import Interval as Interval
from ..utils.parallel import Parallel as Parallel, delayed as delayed
from ..utils.validation import check_is_fitted as check_is_fitted

# Authors: Conrad Lee <conradlee@gmail.com>
#          Alexandre Gramfort <alexandre.gramfort@inria.fr>
#          Gael Varoquaux <gael.varoquaux@normalesup.org>
#          Martino Sorbaro <martino.sorbaro@ed.ac.uk>

def estimate_bandwidth(
    X: MatrixLike,
    *,
    quantile: Float = 0.3,
    n_samples: None | Int = None,
    random_state: RandomState | Int = 0,
    n_jobs: None | Int = None,
) -> Float: ...
def mean_shift(
    X: MatrixLike,
    *,
    bandwidth: None | Float = None,
    seeds: None | MatrixLike = None,
    bin_seeding: bool = False,
    min_bin_freq: Int = 1,
    cluster_all: bool = True,
    max_iter: Int = 300,
    n_jobs: None | Int = None,
) -> tuple[ndarray, ndarray]: ...
def get_bin_seeds(X: MatrixLike, bin_size: Float, min_bin_freq: Int = 1) -> ndarray: ...

class MeanShift(ClusterMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: int = ...
    labels_: ndarray = ...
    cluster_centers_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        bandwidth: None | Float = None,
        seeds: None | MatrixLike = None,
        bin_seeding: bool = False,
        min_bin_freq: Int = 1,
        cluster_all: bool = True,
        n_jobs: None | Int = None,
        max_iter: Int = 300,
    ) -> None: ...
    def fit(self, X: MatrixLike, y: Any = None) -> Self: ...
    def predict(self, X: MatrixLike) -> ndarray: ...
