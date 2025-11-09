__all__ = (
    "PerfTimer",
    "PerfInfo",
)

import time
import typing as t
from dataclasses import dataclass

if t.TYPE_CHECKING:
    ...


@dataclass(slots=True, frozen=True, kw_only=True)
class PerfInfo:
    nano: int

    @property
    def micro(self) -> float:
        return self.nano / 1_000

    @property
    def milli(self) -> float:
        return self.nano / 1_000_000

    @property
    def seconds(self) -> float:
        return self.nano / 1_000_000_000


class PerfTimer:

    def __init__(self):
        self._started_at_ns: int = 0
        self._stopped_at_ns: int = 0

    def __str__(self) -> str:
        return f"timer ({self._started_at_ns}, {self._stopped_at_ns}) ns"

    def __enter__(self):
        self.start()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def start(self):
        self._started_at_ns = time.perf_counter_ns()

    def stop(self):
        self._stopped_at_ns = time.perf_counter_ns()

    def get_info(self) -> "PerfInfo":
        return PerfInfo(nano=self._stopped_at_ns - self._started_at_ns)
