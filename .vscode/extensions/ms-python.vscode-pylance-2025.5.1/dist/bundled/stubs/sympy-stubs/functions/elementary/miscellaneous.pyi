from typing_extensions import Self

from sympy.core import Function
from sympy.core.expr import Expr
from sympy.core.function import Application, Lambda
from sympy.core.operations import LatticeOp
from sympy.core.power import Pow
from sympy.core.singleton import Singleton
from sympy.core.symbol import Dummy
from sympy.functions.elementary.piecewise import Piecewise
from sympy.functions.special.delta_functions import Heaviside
from sympy.series.order import Order

class IdentityFunction(Lambda, metaclass=Singleton):
    _symbol = ...
    @property
    def signature(self) -> tuple: ...
    @property
    def expr(self) -> Dummy: ...

Id = ...

def sqrt(arg, evaluate=...) -> Pow: ...
def cbrt(arg, evaluate=...) -> Pow: ...
def root(arg, n, k=..., evaluate=...) -> Order | Pow: ...
def real_root(arg, n=..., evaluate=...) -> Piecewise: ...

class MinMaxBase(Expr, LatticeOp):
    def __new__(cls, *args, **assumptions) -> Self: ...
    def evalf(self, n=..., **options) -> Self: ...
    def n(self, *args, **kwargs) -> Self: ...

    _eval_is_algebraic = ...
    _eval_is_antihermitian = ...
    _eval_is_commutative = ...
    _eval_is_complex = ...
    _eval_is_composite = ...
    _eval_is_even = ...
    _eval_is_finite = ...
    _eval_is_hermitian = ...
    _eval_is_imaginary = ...
    _eval_is_infinite = ...
    _eval_is_integer = ...
    _eval_is_irrational = ...
    _eval_is_negative = ...
    _eval_is_noninteger = ...
    _eval_is_nonnegative = ...
    _eval_is_nonpositive = ...
    _eval_is_nonzero = ...
    _eval_is_odd = ...
    _eval_is_polar = ...
    _eval_is_positive = ...
    _eval_is_prime = ...
    _eval_is_rational = ...
    _eval_is_real = ...
    _eval_is_extended_real = ...
    _eval_is_transcendental = ...
    _eval_is_zero = ...

class Max(MinMaxBase, Application):
    zero = ...
    identity = ...
    def fdiff(self, argindex) -> Heaviside: ...

class Min(MinMaxBase, Application):
    zero = ...
    identity = ...
    def fdiff(self, argindex) -> Heaviside: ...

class Rem(Function):
    kind = ...
    @classmethod
    def eval(cls, p, q) -> None: ...
