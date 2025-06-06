import warnings
from numbers import Integral as Integral, Real as Real
from typing import Any, ClassVar, Literal
from typing_extensions import Self

import numpy as np
from numpy import ndarray
from numpy.random import RandomState

from .._config import config_context as config_context
from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, ClusterMixin
from ..exceptions import ConvergenceWarning as ConvergenceWarning
from ..metrics import euclidean_distances as euclidean_distances, pairwise_distances_argmin as pairwise_distances_argmin
from ..utils import as_float_array as as_float_array, check_random_state as check_random_state
from ..utils._param_validation import Interval as Interval, StrOptions as StrOptions
from ..utils.validation import check_is_fitted as check_is_fitted

###############################################################################
# Public API

def affinity_propagation(
    S: MatrixLike,
    *,
    preference: float | None | ArrayLike = None,
    convergence_iter: Int = 15,
    max_iter: Int = 200,
    damping: Float = 0.5,
    copy: bool = True,
    verbose: bool = False,
    return_n_iter: bool = False,
    random_state: RandomState | None | Int = None,
) -> tuple[ndarray, ndarray, int] | tuple[ndarray, ndarray]: ...

class AffinityPropagation(ClusterMixin, BaseEstimator):
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...
    n_iter_: int = ...
    affinity_matrix_: ndarray = ...
    labels_: ndarray = ...
    cluster_centers_: ndarray = ...
    cluster_centers_indices_: ndarray = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        *,
        damping: Float = 0.5,
        max_iter: Int = 200,
        convergence_iter: Int = 15,
        copy: bool = True,
        preference: float | None | ArrayLike = None,
        affinity: Literal["euclidean", "precomputed"] = "euclidean",
        verbose: bool = False,
        random_state: RandomState | None | Int = None,
    ) -> None: ...
    def fit(self, X: MatrixLike, y: Any = None) -> Self: ...
    def predict(self, X: MatrixLike | ArrayLike) -> ndarray: ...
    def fit_predict(self, X: MatrixLike, y: Any = None) -> ndarray: ...
