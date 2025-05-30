from collections.abc import Iterable
from typing import Any

import numpy as np
from scipy.sparse import csr_matrix

def get_valid_metric_ids(L: Iterable) -> list[str]: ...

class DistanceMetric:
    def __init__(self) -> None: ...
    @classmethod
    def get_metric(cls, metric: str, **kwargs) -> DistanceMetric: ...
    def dist(self, x1, x2, size): ...
    def rdist(self, x1, x2, size): ...
    def pdist(self, X, D) -> int: ...
    def cdist(self, X, Y, D) -> int: ...
    def dist_csr(self, x1_data, x1_indices, x2_data, x2_indices, x1_start, x1_end, x2_start, x2_end, size): ...
    def rdist_csr(self, x1_data, x1_indices, x2_data, x2_indices, x1_start, x1_end, x2_start, x2_end, size): ...
    def pdist_csr(self, x1_data, x1_indices, x1_indptr, size, D) -> int: ...
    def cdist_csr(self, x1_data, x1_indices, x1_indptr, x2_data, x2_indices, x2_indptr, size, D) -> int: ...
    def rdist_to_dist(self, rdist: float) -> float: ...
    def dist_to_rdist(self, dist: float) -> float: ...
    def pairwise(self, X: np.ndarray | csr_matrix, Y: np.ndarray | csr_matrix | None = None) -> np.ndarray: ...

class DistanceMetric32:
    def __init__(self) -> None: ...
    @classmethod
    def get_metric(cls, metric: str, **kwargs) -> DistanceMetric: ...
    def dist(self, x1, x2, size): ...
    def rdist(self, x1, x2, size): ...
    def pdist(self, X, D) -> int: ...
    def cdist(self, X, Y, D) -> int: ...
    def dist_csr(self, x1_data, x1_indices, x2_data, x2_indices, x1_start, x1_end, x2_start, x2_end, size): ...
    def rdist_csr(self, x1_data, x1_indices, x2_data, x2_indices, x1_start, x1_end, x2_start, x2_end, size): ...
    def pdist_csr(self, x1_data, x1_indices, x1_indptr, size, D) -> int: ...
    def cdist_csr(self, x1_data, x1_indices, x1_indptr, x2_data, x2_indices, x2_indptr, size, D) -> int: ...
    def rdist_to_dist(self, rdist: float) -> float: ...
    def dist_to_rdist(self, dist: float) -> float: ...
    def pairwise(self, X: np.ndarray | csr_matrix, Y: np.ndarray | csr_matrix | None = None) -> np.ndarray: ...

class BrayCurtisDistance(DistanceMetric): ...
class BrayCurtisDistance32(DistanceMetric32): ...
class CanberraDistance(DistanceMetric): ...
class CanberraDistance32(DistanceMetric32): ...
class ChebyshevDistance(DistanceMetric): ...
class ChebyshevDistance32(DistanceMetric32): ...
class DiceDistance(DistanceMetric): ...
class DiceDistance32(DistanceMetric32): ...
class EuclideanDistance(DistanceMetric): ...
class EuclideanDistance32(DistanceMetric32): ...
class HammingDistance(DistanceMetric): ...
class HammingDistance32(DistanceMetric32): ...
class HaversineDistance(DistanceMetric): ...
class HaversineDistance32(DistanceMetric32): ...
class JaccardDistance(DistanceMetric): ...
class JaccardDistance32(DistanceMetric32): ...
class KulsinskiDistance(DistanceMetric): ...
class KulsinskiDistance32(DistanceMetric32): ...
class MahalanobisDistance(DistanceMetric): ...
class MahalanobisDistance32(DistanceMetric32): ...
class ManhattanDistance(DistanceMetric): ...
class ManhattanDistance32(DistanceMetric32): ...
class MatchingDistance(DistanceMetric): ...
class MatchingDistance32(DistanceMetric32): ...
class MinkowskiDistance(DistanceMetric): ...
class MinkowskiDistance32(DistanceMetric32): ...
class PyFuncDistance(DistanceMetric): ...
class PyFuncDistance32(DistanceMetric32): ...
class RogersTanimotoDistance(DistanceMetric): ...
class RogersTanimotoDistance32(DistanceMetric32): ...
class RussellRaoDistance(DistanceMetric): ...
class RussellRaoDistance32(DistanceMetric32): ...
class SEuclideanDistance(DistanceMetric): ...
class SEuclideanDistance32(DistanceMetric32): ...
class SokalMichenerDistance(DistanceMetric): ...
class SokalMichenerDistance32(DistanceMetric32): ...
class SokalSneathDistance(DistanceMetric): ...
class SokalSneathDistance32(DistanceMetric32): ...
class WMinkowskiDistance(DistanceMetric): ...
class WMinkowskiDistance32(DistanceMetric32): ...

METRIC_MAPPING: dict[str, Any]
