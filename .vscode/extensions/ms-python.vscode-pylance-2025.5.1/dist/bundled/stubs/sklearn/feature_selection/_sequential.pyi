import warnings
from collections.abc import Iterable
from numbers import Integral as Integral, Real as Real
from typing import Callable, ClassVar, Literal
from typing_extensions import Self

import numpy as np
from numpy import ndarray

from .._typing import ArrayLike, Float, Int, MatrixLike
from ..base import BaseEstimator, MetaEstimatorMixin, clone as clone
from ..metrics import get_scorer_names as get_scorer_names
from ..model_selection import BaseCrossValidator, cross_val_score as cross_val_score
from ..utils._param_validation import HasMethods as HasMethods, Hidden as Hidden, Interval as Interval, StrOptions as StrOptions
from ..utils.validation import check_is_fitted as check_is_fitted
from ._base import SelectorMixin

class SequentialFeatureSelector(SelectorMixin, MetaEstimatorMixin, BaseEstimator):
    support_: ndarray = ...
    n_features_to_select_: int = ...
    feature_names_in_: ndarray = ...
    n_features_in_: int = ...

    _parameter_constraints: ClassVar[dict] = ...

    def __init__(
        self,
        estimator: BaseEstimator,
        *,
        n_features_to_select: float | Literal["auto", "warn"] = "warn",
        tol: None | Float = None,
        direction: Literal["forward", "backward"] = "forward",
        scoring: None | str | Callable = None,
        cv: Iterable | int | BaseCrossValidator = 5,
        n_jobs: None | Int = None,
    ) -> None: ...
    def fit(self, X: MatrixLike, y: None | ArrayLike = None) -> Self: ...
