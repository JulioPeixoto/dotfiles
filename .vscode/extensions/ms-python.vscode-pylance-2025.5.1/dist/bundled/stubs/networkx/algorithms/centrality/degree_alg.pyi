from collections.abc import Mapping

from ...classes.graph import Graph
from ...utils.decorators import not_implemented_for

__all__ = ["degree_centrality", "in_degree_centrality", "out_degree_centrality"]

def degree_centrality(G: Graph) -> Mapping: ...
def in_degree_centrality(G: Graph) -> Mapping: ...
def out_degree_centrality(G: Graph) -> Mapping: ...
