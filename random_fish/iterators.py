__all__ = (
    "RandomFishIterator",
    "LengthType",
)

import logging
import typing as t

from random_fish.base import RandomSchoolOfFishInterface

if t.TYPE_CHECKING:
    from random_fish.base import RandomFishInterface


logger = logging.getLogger(__name__)

LengthType = t.Union[int, "RandomFishInterface[int]"]

ItemTypeVar = t.TypeVar("ItemTypeVar")


class RandomFishIterator(
    RandomSchoolOfFishInterface[ItemTypeVar], t.Generic[ItemTypeVar]
):
    def __init__(
        self, item: "RandomFishInterface[ItemTypeVar]", len: LengthType
    ):
        self._len = len
        self._fish = item

    def __iter__(self) -> t.Iterator[ItemTypeVar]:
        _len = self._get_len()
        for _i in range(_len):
            val = next(self._fish)
            if __debug__:
                logger.debug(
                    "instance: %r. %r/%r. value: %r", self, _i, _len, val
                )
            yield val

    async def __aiter__(self) -> t.AsyncIterator[ItemTypeVar]:
        _len = self._get_len()
        for _i in range(_len):
            val = await anext(self._fish)
            if __debug__:
                logger.debug(
                    "instance: %r. %r/%r. value: %r", self, _i, _len, val
                )
            yield val

    def _get_len(self) -> int:
        if isinstance(self._len, int):
            return self._len
        return next(self._len)
