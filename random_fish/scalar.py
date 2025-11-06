__all__ = (
    "RandBool",
    "RandInt",
    "RandFloat",
    "RandTuple",
)

import logging
import typing as t
from random import choice, randint, uniform

from .base import RandomValueGeneratorInterface

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


class RandBool(RandomValueGeneratorInterface[bool]):
    _values = [True, False]

    def run(self) -> bool:
        value = choice(self._values)
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value


class RandInt(RandomValueGeneratorInterface[int]):
    def __init__(self, min: int, max: int):
        self._min_val = min
        self._max_val = max

    def run(self) -> int:
        value = randint(self._min_val, self._max_val)
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value


class RandFloat(RandomValueGeneratorInterface[float]):
    def __init__(self, min: float, max: float):
        self._min_val = min
        self._max_val = max

    def run(self) -> float:
        value = uniform(self._min_val, self._max_val)
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value


TupleTypeVar = t.TypeVar("TupleTypeVar", bound=tuple)


class RandTuple(
    RandomValueGeneratorInterface[TupleTypeVar], t.Generic[TupleTypeVar]
):
    def __init__(self, *args: "RandomValueGeneratorInterface"):
        self._generators = args

    def run(self) -> TupleTypeVar:
        value = tuple([g.run() for g in self._generators])
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value  # type: ignore[return-value]
