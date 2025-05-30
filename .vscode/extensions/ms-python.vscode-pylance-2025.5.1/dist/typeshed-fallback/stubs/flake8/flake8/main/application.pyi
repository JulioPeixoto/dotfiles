from _typeshed import Incomplete
from collections.abc import Sequence
from logging import Logger

LOG: Logger

class Application:
    start_time: Incomplete
    end_time: Incomplete
    plugins: Incomplete
    formatter: Incomplete
    guide: Incomplete
    file_checker_manager: Incomplete
    options: Incomplete
    result_count: int
    total_result_count: int
    catastrophic_failure: bool
    def __init__(self) -> None: ...
    def exit_code(self) -> int: ...
    def make_formatter(self) -> None: ...
    def make_guide(self) -> None: ...
    def make_file_checker_manager(self, argv: Sequence[str]) -> None: ...
    def run_checks(self) -> None: ...
    def report_benchmarks(self) -> None: ...
    def report_errors(self) -> None: ...
    def report_statistics(self) -> None: ...
    def initialize(self, argv: Sequence[str]) -> None: ...
    def report(self) -> None: ...
    def run(self, argv: Sequence[str]) -> None: ...
