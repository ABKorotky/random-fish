__all__ = (
    "RandomBool",
    "RandomInt",
    "RandomFloat",
)

import logging
import random
import typing as t

from random_fish.base import RandomFishInterface

if t.TYPE_CHECKING:
    ...


logger = logging.getLogger(__name__)


class RandomBool(RandomFishInterface[bool]):
    _values = (True, False)

    def __next__(self) -> bool:
        val = random.choice(self._values)
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    async def __anext__(self) -> bool:
        return self.__next__()


class RandomInt(RandomFishInterface[int]):
    def __init__(self, min: int, max: int):
        self._min = min
        self._max = max

    def __next__(self) -> int:
        val = random.randint(self._min, self._max)
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    async def __anext__(self) -> int:
        return self.__next__()


class RandomFloat(RandomFishInterface[float]):
    def __init__(self, min: float, max: float):
        self._min = min
        self._max = max

    def __next__(self) -> float:
        val = random.uniform(self._min, self._max)
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    async def __anext__(self) -> float:
        return self.__next__()
