__all__ = ("RandomDateTime",)

import datetime
import logging
import typing as t

from random_fish.base import RandomFishInterface
from random_fish.scalar import RandomInt

if t.TYPE_CHECKING:
    ...


logger = logging.getLogger(__name__)


class RandomDateTime(RandomFishInterface["datetime.datetime"]):
    def __init__(self, min: "datetime.datetime", max: "datetime.datetime"):
        self._fish = RandomInt(int(min.timestamp()), int(max.timestamp()))

    def __next__(self) -> "datetime.datetime":
        ts = next(self._fish)
        return datetime.datetime.fromtimestamp(ts)

    async def __anext__(self) -> "datetime.datetime":
        ts = await anext(self._fish)
        return datetime.datetime.fromtimestamp(ts)
