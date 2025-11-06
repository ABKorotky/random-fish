__all__ = (
    "RandBool",
    "RandInt",
    "RandFloat",
    "RandTuple",
)

import logging
import typing as t
from random import choice, randint, uniform

from .base import RandomValueBuilderInterface

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


class RandBool(RandomValueBuilderInterface[bool]):
    _values = [True, False]

    def run(self) -> bool:
        value = choice(self._values)
        logger.debug("value: %r.", value)
        return value


class RandInt(RandomValueBuilderInterface[int]):
    def __init__(self, min: int, max: int):
        self._min_val = min
        self._max_val = max

    def run(self) -> int:
        value = randint(self._min_val, self._max_val)
        logger.debug("value: %r.", value)
        return value


class RandFloat(RandomValueBuilderInterface[float]):
    def __init__(self, min: float, max: float):
        self._min_val = min
        self._max_val = max

    def run(self) -> float:
        value = uniform(self._min_val, self._max_val)
        logger.debug("value: %r.", value)
        return value


TupleTypeVar = t.TypeVar("TupleTypeVar", bound=tuple)


class RandTuple(
    RandomValueBuilderInterface[TupleTypeVar], t.Generic[TupleTypeVar]
):
    def __init__(self, *args: "RandomValueBuilderInterface"):
        self._generators = args

    def run(self) -> TupleTypeVar:
        value = tuple([g.run() for g in self._generators])
        logger.debug("value: %r.", value)
        return value  # type: ignore[return-value]
