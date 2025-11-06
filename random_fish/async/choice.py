__all__ = (
    "AsyncRandChoice",
    "AsyncRandIntChoice",
)

import logging
import typing as t
from random import choice

from .base import AsyncRandomValueGeneratorInterface

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)

ValueTypeVar = t.TypeVar("ValueTypeVar")


class AsyncRandChoice(
    AsyncRandomValueGeneratorInterface[ValueTypeVar], t.Generic[ValueTypeVar]
):

    def __init__(self, *args: ValueTypeVar):
        self._values = args

    async def run(self) -> ValueTypeVar:
        value = choice(self._values)
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value


class AsyncRandIntChoice(AsyncRandChoice[int]): ...
