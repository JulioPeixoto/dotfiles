from collections.abc import Mapping
from typing import Any

from ..classes.graph import Graph
from ..utils import py_random_state

__all__ = ["random_internet_as_graph"]

def uniform_int_from_avg(a, m, seed): ...
def choose_pref_attach(degs: Mapping, seed) -> Any: ...

class AS_graph_generator:
    def __init__(self, n, seed): ...
    def t_graph(self): ...
    def add_edge(self, i, j, kind): ...
    def choose_peer_pref_attach(self, node_list): ...
    def choose_node_pref_attach(self, node_list): ...
    def add_customer(self, i, j): ...
    def add_node(self, i: Any, kind: str, reg2prob: float, avg_deg: float, t_edge_prob: float) -> Any: ...
    def add_m_peering_link(self, m: Any, to_kind: str) -> bool: ...
    def add_cp_peering_link(self, cp: Any, to_kind: str) -> bool: ...
    def graph_regions(self, rn): ...
    def add_peering_links(self, from_kind, to_kind): ...
    def generate(self): ...

@py_random_state(1)
def random_internet_as_graph(n, seed=None): ...
