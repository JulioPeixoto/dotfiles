from . import cluster as cluster
from ._classification import (
    accuracy_score as accuracy_score,
    balanced_accuracy_score as balanced_accuracy_score,
    brier_score_loss as brier_score_loss,
    class_likelihood_ratios as class_likelihood_ratios,
    classification_report as classification_report,
    cohen_kappa_score as cohen_kappa_score,
    confusion_matrix as confusion_matrix,
    f1_score as f1_score,
    fbeta_score as fbeta_score,
    hamming_loss as hamming_loss,
    hinge_loss as hinge_loss,
    jaccard_score as jaccard_score,
    log_loss as log_loss,
    matthews_corrcoef as matthews_corrcoef,
    multilabel_confusion_matrix as multilabel_confusion_matrix,
    precision_recall_fscore_support as precision_recall_fscore_support,
    precision_score as precision_score,
    recall_score as recall_score,
    zero_one_loss as zero_one_loss,
)
from ._dist_metrics import DistanceMetric as DistanceMetric
from ._plot.confusion_matrix import ConfusionMatrixDisplay as ConfusionMatrixDisplay
from ._plot.det_curve import DetCurveDisplay as DetCurveDisplay
from ._plot.precision_recall_curve import PrecisionRecallDisplay as PrecisionRecallDisplay
from ._plot.regression import PredictionErrorDisplay as PredictionErrorDisplay
from ._plot.roc_curve import RocCurveDisplay as RocCurveDisplay
from ._ranking import (
    auc as auc,
    average_precision_score as average_precision_score,
    coverage_error as coverage_error,
    dcg_score as dcg_score,
    det_curve as det_curve,
    label_ranking_average_precision_score as label_ranking_average_precision_score,
    label_ranking_loss as label_ranking_loss,
    ndcg_score as ndcg_score,
    precision_recall_curve as precision_recall_curve,
    roc_auc_score as roc_auc_score,
    roc_curve as roc_curve,
    top_k_accuracy_score as top_k_accuracy_score,
)
from ._regression import (
    d2_absolute_error_score as d2_absolute_error_score,
    d2_pinball_score as d2_pinball_score,
    d2_tweedie_score as d2_tweedie_score,
    explained_variance_score as explained_variance_score,
    max_error as max_error,
    mean_absolute_error as mean_absolute_error,
    mean_absolute_percentage_error as mean_absolute_percentage_error,
    mean_gamma_deviance as mean_gamma_deviance,
    mean_pinball_loss as mean_pinball_loss,
    mean_poisson_deviance as mean_poisson_deviance,
    mean_squared_error as mean_squared_error,
    mean_squared_log_error as mean_squared_log_error,
    mean_tweedie_deviance as mean_tweedie_deviance,
    median_absolute_error as median_absolute_error,
    r2_score as r2_score,
    root_mean_squared_error as root_mean_squared_error,
    root_mean_squared_log_error as root_mean_squared_log_error,
)
from ._scorer import (
    SCORERS as SCORERS,
    check_scoring as check_scoring,
    get_scorer as get_scorer,
    get_scorer_names as get_scorer_names,
    make_scorer as make_scorer,
)
from .cluster import (
    adjusted_mutual_info_score as adjusted_mutual_info_score,
    adjusted_rand_score as adjusted_rand_score,
    calinski_harabasz_score as calinski_harabasz_score,
    completeness_score as completeness_score,
    consensus_score as consensus_score,
    davies_bouldin_score as davies_bouldin_score,
    fowlkes_mallows_score as fowlkes_mallows_score,
    homogeneity_completeness_v_measure as homogeneity_completeness_v_measure,
    homogeneity_score as homogeneity_score,
    mutual_info_score as mutual_info_score,
    normalized_mutual_info_score as normalized_mutual_info_score,
    pair_confusion_matrix as pair_confusion_matrix,
    rand_score as rand_score,
    silhouette_samples as silhouette_samples,
    silhouette_score as silhouette_score,
    v_measure_score as v_measure_score,
)
from .pairwise import (
    euclidean_distances as euclidean_distances,
    nan_euclidean_distances as nan_euclidean_distances,
    pairwise_distances as pairwise_distances,
    pairwise_distances_argmin as pairwise_distances_argmin,
    pairwise_distances_argmin_min as pairwise_distances_argmin_min,
    pairwise_distances_chunked as pairwise_distances_chunked,
    pairwise_kernels as pairwise_kernels,
)

__all__ = [
    "accuracy_score",
    "adjusted_mutual_info_score",
    "adjusted_rand_score",
    "auc",
    "average_precision_score",
    "balanced_accuracy_score",
    "calinski_harabasz_score",
    "check_scoring",
    "class_likelihood_ratios",
    "classification_report",
    "cluster",
    "cohen_kappa_score",
    "completeness_score",
    "ConfusionMatrixDisplay",
    "confusion_matrix",
    "consensus_score",
    "coverage_error",
    "d2_tweedie_score",
    "d2_absolute_error_score",
    "d2_pinball_score",
    "dcg_score",
    "davies_bouldin_score",
    "DetCurveDisplay",
    "det_curve",
    "DistanceMetric",
    "euclidean_distances",
    "explained_variance_score",
    "f1_score",
    "fbeta_score",
    "fowlkes_mallows_score",
    "get_scorer",
    "hamming_loss",
    "hinge_loss",
    "homogeneity_completeness_v_measure",
    "homogeneity_score",
    "jaccard_score",
    "label_ranking_average_precision_score",
    "label_ranking_loss",
    "log_loss",
    "make_scorer",
    "nan_euclidean_distances",
    "matthews_corrcoef",
    "max_error",
    "mean_absolute_error",
    "mean_squared_error",
    "mean_squared_log_error",
    "mean_pinball_loss",
    "mean_poisson_deviance",
    "mean_gamma_deviance",
    "mean_tweedie_deviance",
    "median_absolute_error",
    "mean_absolute_percentage_error",
    "multilabel_confusion_matrix",
    "mutual_info_score",
    "ndcg_score",
    "normalized_mutual_info_score",
    "pair_confusion_matrix",
    "pairwise_distances",
    "pairwise_distances_argmin",
    "pairwise_distances_argmin_min",
    "pairwise_distances_chunked",
    "pairwise_kernels",
    "PrecisionRecallDisplay",
    "precision_recall_curve",
    "precision_recall_fscore_support",
    "precision_score",
    "PredictionErrorDisplay",
    "r2_score",
    "rand_score",
    "recall_score",
    "RocCurveDisplay",
    "roc_auc_score",
    "roc_curve",
    "root_mean_squared_error",
    "root_mean_squared_log_error",
    "SCORERS",
    "get_scorer_names",
    "silhouette_samples",
    "silhouette_score",
    "top_k_accuracy_score",
    "v_measure_score",
    "zero_one_loss",
    "brier_score_loss",
]
