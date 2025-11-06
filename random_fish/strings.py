__all__ = ("RandString",)

import logging
import typing as t
from random import choice
from string import ascii_letters

from .base import BaseRandCollectionGenerator

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


class RandString(BaseRandCollectionGenerator[str]):
    def __init__(self, chars: str = ascii_letters, **kwargs):
        super().__init__(**kwargs)
        self._chars = chars

    def run(self) -> str:
        _len = self._get_rand_len()
        value = "".join(choice(self._chars) for _ in range(_len))
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value
