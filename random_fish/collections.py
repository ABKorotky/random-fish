__all__ = (
    "BaseRandomSequence",
    "RandomList",
    "RandomSet",
    "RandomMap",
)

import logging
import typing as t

from random_fish.base import RandomFishInterface, RandomSchoolOfFishInterface
from random_fish.iterators import RandomFishIterator
from random_fish.structural import RandomTuple

if t.TYPE_CHECKING:
    from random_fish.iterators import LengthType


logger = logging.getLogger(__name__)

ItemTypeVar = t.TypeVar("ItemTypeVar")
ContainerTypeVar = t.TypeVar("ContainerTypeVar")


class BaseRandomSequence(
    RandomFishInterface[ContainerTypeVar],
    RandomSchoolOfFishInterface[ItemTypeVar],
    t.Generic[ContainerTypeVar, ItemTypeVar],
):
    def __init__(
        self, item: "RandomFishInterface[ItemTypeVar]", len: "LengthType"
    ):
        self._iterator = RandomFishIterator[ItemTypeVar](item=item, len=len)

    def __iter__(self) -> t.Iterator[ItemTypeVar]:
        return self._iterator.__iter__()

    def __aiter__(self) -> t.AsyncIterator[ItemTypeVar]:
        return self._iterator.__aiter__()


class RandomList(BaseRandomSequence[list, ItemTypeVar], t.Generic[ItemTypeVar]):
    def __next__(self) -> list[ItemTypeVar]:
        val = list(self)
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    async def __anext__(self) -> list[ItemTypeVar]:
        val = [i async for i in self]
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val


class RandomSet(BaseRandomSequence[set, ItemTypeVar], t.Generic[ItemTypeVar]):
    def __next__(self) -> set[ItemTypeVar]:
        val = set(self)
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    async def __anext__(self) -> set[ItemTypeVar]:
        val = set([i async for i in self])
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val


KeyTypeVar = t.TypeVar("KeyTypeVar")
ValueTypeVar = t.TypeVar("ValueTypeVar")


class RandomMap(
    RandomFishInterface,
    RandomSchoolOfFishInterface,
    t.Generic[KeyTypeVar, ValueTypeVar],
):
    def __init__(
        self,
        len: "LengthType",
        key: "RandomFishInterface[KeyTypeVar]",
        value: "RandomFishInterface[ValueTypeVar]",
    ):
        self._iterator = RandomFishIterator[tuple[KeyTypeVar, ValueTypeVar]](
            item=RandomTuple(key, value), len=len
        )

    def __next__(self) -> dict[KeyTypeVar, ValueTypeVar]:
        val = dict(self)
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    async def __anext__(self) -> dict[KeyTypeVar, ValueTypeVar]:
        val = {k: v for k, v in self}
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    def __iter__(self) -> t.Iterator[tuple[KeyTypeVar, ValueTypeVar]]:
        return self._iterator.__iter__()

    def __aiter__(
        self,
    ) -> t.AsyncIterator[tuple[KeyTypeVar, ValueTypeVar]]:
        return self._iterator.__aiter__()
