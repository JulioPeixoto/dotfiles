from collections.abc import Generator, Iterator
from typing import Any
from typing_extensions import Self

from sympy.polys.polyutils import PicklableWithSlots
from sympy.series.order import Order
from sympy.utilities import public

@public
def itermonomials(variables, max_degrees, min_degrees=...) -> Generator[Any | Order, Any, None]: ...
def monomial_count(V, N): ...
def monomial_mul(A, B) -> tuple[Any, ...]: ...
def monomial_div(A, B) -> tuple[Any, ...] | None: ...
def monomial_ldiv(A, B) -> tuple[Any, ...]: ...
def monomial_pow(A, n) -> tuple[Any, ...]: ...
def monomial_gcd(A, B) -> tuple[Any, ...]: ...
def monomial_lcm(A, B) -> tuple[Any, ...]: ...
def monomial_divides(A, B) -> bool: ...
def monomial_max(*monoms) -> tuple[Any, ...]: ...
def monomial_min(*monoms) -> tuple[Any, ...]: ...
def monomial_deg(M) -> int: ...
def term_div(a, b, domain) -> tuple[tuple[Any, ...], Any] | None: ...

class MonomialOps:
    def __init__(self, ngens) -> None: ...
    def mul(self): ...
    def pow(self): ...
    def mulpow(self): ...
    def ldiv(self): ...
    def div(self): ...
    def lcm(self): ...
    def gcd(self): ...

@public
class Monomial(PicklableWithSlots):
    __slots__ = ...
    def __init__(self, monom, gens=...) -> None: ...
    def rebuild(self, exponents, gens=...) -> Self: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
    def __getitem__(self, item): ...
    def __hash__(self) -> int: ...
    def as_expr(self, *gens) -> Order: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __mul__(self, other) -> Self: ...
    def __truediv__(self, other) -> Self: ...

    __floordiv__ = ...
    def __pow__(self, other) -> Self: ...
    def gcd(self, other) -> Self: ...
    def lcm(self, other) -> Self: ...
