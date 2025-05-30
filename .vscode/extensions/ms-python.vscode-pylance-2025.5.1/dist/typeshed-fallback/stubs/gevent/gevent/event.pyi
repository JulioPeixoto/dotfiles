from types import TracebackType
from typing import Generic, Literal, Protocol, TypeVar, overload
from typing_extensions import TypeAlias

from gevent._abstract_linkable import AbstractLinkable

_T = TypeVar("_T")
_T_co = TypeVar("_T_co", covariant=True)
# gevent generally allows the tracebock to be omitted, it can also fail to serialize
# in which case it will be None as well.
_ExcInfo: TypeAlias = tuple[type[BaseException], BaseException, TracebackType | None]
_OptExcInfo: TypeAlias = _ExcInfo | tuple[None, None, None]

class _ValueSource(Protocol[_T_co]):
    def successful(self) -> bool: ...
    @property
    def value(self) -> _T_co | None: ...
    @property
    def exception(self) -> BaseException | None: ...

class Event(AbstractLinkable):
    def __init__(self) -> None: ...
    def is_set(self) -> bool: ...
    def isSet(self) -> bool: ...
    def ready(self) -> bool: ...
    def set(self) -> None: ...
    def clear(self) -> None: ...
    @overload
    def wait(self, timeout: None = None) -> Literal[True]: ...
    @overload
    def wait(self, timeout: float) -> bool: ...

class AsyncResult(AbstractLinkable, Generic[_T]):
    def __init__(self) -> None: ...
    @property
    def value(self) -> _T | None: ...
    @property
    def exc_info(self) -> _OptExcInfo | tuple[None, None, None] | tuple[()]: ...
    @property
    def exception(self) -> BaseException | None: ...
    def ready(self) -> bool: ...
    def successful(self) -> bool: ...
    def set(self, value: _T | None = None) -> None: ...
    @overload
    def set_exception(self, exception: BaseException, exc_info: None = None) -> None: ...
    @overload
    def set_exception(self, exception: BaseException | None, exc_info: _OptExcInfo) -> None: ...
    # technically get/get_nowait/result should just return _T, but the API is designed in
    # such a way that it is perfectly legal for a ValueSource to have neither its value nor
    # its exception set, while still being marked successful, at which point None would be
    # stored into value, it's also legal to call set without arguments, which has the same
    # effect, this is a little annoying, since it will introduce some additional None checks
    # that may not be necessary, but it's impossible to annotate this situation, so for now
    # we just deal with the possibly redundant None checks...
    def get(self, block: bool = True, timeout: float | None = None) -> _T | None: ...
    def get_nowait(self) -> _T | None: ...
    def wait(self, timeout: float | None = None) -> _T | None: ...
    def __call__(self, source: _ValueSource[_T]) -> None: ...
    def result(self, timeout: float | None = None) -> _T | None: ...
    set_result = set
    def done(self) -> bool: ...
    def cancel(self) -> Literal[False]: ...
    def cancelled(self) -> Literal[False]: ...

__all__ = ["Event", "AsyncResult"]
