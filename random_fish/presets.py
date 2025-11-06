__all__ = ("RandText",)

import logging
import typing as t

from .base import BaseRandCollectionGenerator
from .collections import RandList

if t.TYPE_CHECKING:
    ...


logger = logging.getLogger(__name__)


class RandText(BaseRandCollectionGenerator[str]):

    def __init__(self, word: "BaseRandCollectionGenerator[str]", **kwargs):
        super().__init__(**kwargs)
        self._word_generator = word

    def run(self) -> str:
        _words_gen = RandList(len=self._len, item=self._word_generator)
        value = " ".join(_words_gen.run())
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value
