__all__ = (
    "RandomString",
    "RandomWord",
    "RandomTemplatedString",
    "RandomText",
)

import logging
import typing as t
from string import ascii_letters

from random_fish.base import RandomFishInterface
from random_fish.choice import RandomChoice
from random_fish.iterators import RandomFishIterator

if t.TYPE_CHECKING:
    from random_fish.iterators import LengthType


logger = logging.getLogger(__name__)


class RandomString(RandomFishInterface[str]):

    def __init__(self, len: "LengthType", chars: str):
        self._iterator = RandomFishIterator[str](
            item=RandomChoice(*chars), len=len
        )

    def __next__(self) -> str:
        val = "".join([i for i in self._iterator])
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    async def __anext__(self) -> str:
        return self.__next__()


class RandomWord(RandomString):
    def __init__(self, len: "LengthType"):
        super().__init__(len=len, chars=ascii_letters)


class RandomTemplatedString(RandomFishInterface[str]):
    def __init__(
        self,
        template: str,
        *args: "RandomFishInterface[str]",
        **kwargs: "RandomFishInterface[str]",
    ):
        self._template = template
        self._fishes = args
        self._named_fishes = kwargs

    def __next__(self) -> str:
        placeholders = [next(fish) for fish in self._fishes]
        named_placeholders = {
            name: next(fish) for name, fish in self._named_fishes.items()
        }
        val = self._template.format(*placeholders, **named_placeholders)
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    async def __anext__(self) -> str:
        return self.__next__()


class RandomText(RandomFishInterface[str]):
    def __init__(self, len: "LengthType", word: RandomFishInterface[str]):
        self._iterator = RandomFishIterator[str](item=word, len=len)

    def __next__(self) -> str:
        val = " ".join([i for i in self._iterator])
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    async def __anext__(self) -> str:
        val = " ".join([i async for i in self._iterator])
        if __debug__:
            logger.debug("instance: %r. value: %r", self, val)
        return val
