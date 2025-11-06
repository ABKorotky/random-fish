__all__ = (
    "AsyncRandChoice",
    "AsyncRandIntChoice",
)

import logging
import typing as t
from random import choice

from .base import AsyncRandomValueBuilderInterface

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)

ValueTypeVar = t.TypeVar("ValueTypeVar")


class AsyncRandChoice(
    AsyncRandomValueBuilderInterface[ValueTypeVar], t.Generic[ValueTypeVar]
):

    def __init__(self, *args: ValueTypeVar):
        self._values = args

    async def run(self) -> ValueTypeVar:
        value = choice(self._values)
        logger.debug("value: %r.", value)
        return value


class AsyncRandIntChoice(AsyncRandChoice[int]): ...
