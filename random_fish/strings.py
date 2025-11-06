__all__ = (
    "RandString",
    "RandText",
)

import logging
import typing as t
from string import ascii_letters

from .base import RandomValueBuilderInterface
from .choice import RandChoice
from .collections import RandSequenceGenerator

if t.TYPE_CHECKING:
    from .collections import LengthType

logger = logging.getLogger(__name__)


class RandString(RandomValueBuilderInterface[str]):
    def __init__(self, len: "LengthType", chars: str = ascii_letters):
        self._gen = RandSequenceGenerator(len=len, item=RandChoice(*chars))

    def run(self) -> str:
        value = "".join(list(self._gen.run()))
        logger.debug("value: %r.", value)
        return value


class RandText(RandomValueBuilderInterface[str]):

    def __init__(
        self, len: "LengthType", word: "RandomValueBuilderInterface[str]"
    ):
        self._gen = RandSequenceGenerator(len=len, item=word)

    def run(self) -> str:
        value = " ".join(list(self._gen.run()))
        logger.debug("value: %r.", value)
        return value
