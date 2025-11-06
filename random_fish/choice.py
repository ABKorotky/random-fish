__all__ = (
    "RandChoice",
    "RandIntChoice",
)

import logging
import typing as t
from random import choice

from .base import RandomValueBuilderInterface

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)

ValueTypeVar = t.TypeVar("ValueTypeVar")


class RandChoice(
    RandomValueBuilderInterface[ValueTypeVar], t.Generic[ValueTypeVar]
):

    def __init__(self, *args: ValueTypeVar):
        self._values = args

    def run(self) -> ValueTypeVar:
        value = choice(self._values)
        logger.debug("value: %r.", value)
        return value


class RandIntChoice(RandChoice[int]): ...
