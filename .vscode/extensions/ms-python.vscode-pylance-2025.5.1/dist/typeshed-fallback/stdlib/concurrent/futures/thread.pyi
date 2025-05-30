import queue
from collections.abc import Callable, Iterable, Mapping, Set as AbstractSet
from threading import Lock, Semaphore, Thread
from types import GenericAlias
from typing import Any, Generic, TypeVar, overload
from typing_extensions import TypeVarTuple, Unpack
from weakref import ref

from ._base import BrokenExecutor, Executor, Future

_Ts = TypeVarTuple("_Ts")

_threads_queues: Mapping[Any, Any]
_shutdown: bool
_global_shutdown_lock: Lock

def _python_exit() -> None: ...

_S = TypeVar("_S")

class _WorkItem(Generic[_S]):
    future: Future[_S]
    fn: Callable[..., _S]
    args: Iterable[Any]
    kwargs: Mapping[str, Any]
    def __init__(self, future: Future[_S], fn: Callable[..., _S], args: Iterable[Any], kwargs: Mapping[str, Any]) -> None: ...
    def run(self) -> None: ...
    def __class_getitem__(cls, item: Any, /) -> GenericAlias: ...

def _worker(
    executor_reference: ref[Any],
    work_queue: queue.SimpleQueue[Any],
    initializer: Callable[[Unpack[_Ts]], object],
    initargs: tuple[Unpack[_Ts]],
) -> None: ...

class BrokenThreadPool(BrokenExecutor): ...

class ThreadPoolExecutor(Executor):
    _max_workers: int
    _idle_semaphore: Semaphore
    _threads: AbstractSet[Thread]
    _broken: bool
    _shutdown: bool
    _shutdown_lock: Lock
    _thread_name_prefix: str | None
    _initializer: Callable[..., None] | None
    _initargs: tuple[Any, ...]
    _work_queue: queue.SimpleQueue[_WorkItem[Any]]
    @overload
    def __init__(
        self,
        max_workers: int | None = None,
        thread_name_prefix: str = "",
        initializer: Callable[[], object] | None = None,
        initargs: tuple[()] = (),
    ) -> None: ...
    @overload
    def __init__(
        self,
        max_workers: int | None = None,
        thread_name_prefix: str = "",
        *,
        initializer: Callable[[Unpack[_Ts]], object],
        initargs: tuple[Unpack[_Ts]],
    ) -> None: ...
    @overload
    def __init__(
        self,
        max_workers: int | None,
        thread_name_prefix: str,
        initializer: Callable[[Unpack[_Ts]], object],
        initargs: tuple[Unpack[_Ts]],
    ) -> None: ...
    def _adjust_thread_count(self) -> None: ...
    def _initializer_failed(self) -> None: ...
