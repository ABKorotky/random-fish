__all__ = (
    "RandomChoice",
    "RandomEnumChoice",
)

import logging
import random
import typing as t
from enum import Enum

from random_fish.base import RandomFishInterface

if t.TYPE_CHECKING:
    ...


logger = logging.getLogger(__name__)


ValueTypeVar = t.TypeVar("ValueTypeVar")


class BaseRandomChoice(
    RandomFishInterface[ValueTypeVar], t.Generic[ValueTypeVar]
):
    _choices: tuple[ValueTypeVar, ...]

    def __next__(self) -> ValueTypeVar:
        val = random.choice(self._choices)
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    async def __anext__(self) -> ValueTypeVar:
        return self.__next__()


class RandomChoice(BaseRandomChoice[ValueTypeVar], t.Generic[ValueTypeVar]):
    def __init__(self, *choices: ValueTypeVar):
        self._choices = choices


EnumTypeVar = t.TypeVar("EnumTypeVar", bound=Enum)


class RandomEnumChoice(BaseRandomChoice[EnumTypeVar], t.Generic[EnumTypeVar]):

    def __init__(self, enum: type[EnumTypeVar]):
        self._choices = tuple(list(enum))
