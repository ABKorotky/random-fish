__all__ = (
    "AsyncRandBool",
    "AsyncRandInt",
    "AsyncRandFloat",
    "AsyncRandTuple",
)

import logging
import typing as t
from random import choice, randint, uniform

from .base import AsyncRandomValueGeneratorInterface

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


class AsyncRandBool(AsyncRandomValueGeneratorInterface[bool]):
    _values = [True, False]

    async def run(self) -> bool:
        value = choice(self._values)
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value


class AsyncRandInt(AsyncRandomValueGeneratorInterface[int]):
    def __init__(self, min: int, max: int):
        self._min_val = min
        self._max_val = max

    async def run(self) -> int:
        value = randint(self._min_val, self._max_val)
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value


class AsyncRandFloat(AsyncRandomValueGeneratorInterface[float]):
    def __init__(self, min: float, max: float):
        self._min_val = min
        self._max_val = max

    async def run(self) -> float:
        value = uniform(self._min_val, self._max_val)
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value


TupleTypeVar = t.TypeVar("TupleTypeVar", bound=tuple)


class AsyncRandTuple(
    AsyncRandomValueGeneratorInterface[TupleTypeVar], t.Generic[TupleTypeVar]
):
    def __init__(self, *args: "AsyncRandomValueGeneratorInterface"):
        self._generators = args

    async def run(self) -> TupleTypeVar:
        value = tuple([await g.run() for g in self._generators])
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value  # type: ignore[return-value]
