__all__ = ("AsyncRandText",)

import logging
import typing as t

from .base import BaseAsyncRandCollectionGenerator
from .collections import AsyncRandList

if t.TYPE_CHECKING:
    ...


logger = logging.getLogger(__name__)


class AsyncRandText(BaseAsyncRandCollectionGenerator[str]):

    def __init__(self, word: "BaseAsyncRandCollectionGenerator[str]", **kwargs):
        super().__init__(**kwargs)
        self._word_generator = word

    async def run(self) -> str:
        _words_gen = AsyncRandList(len=self._len, item=self._word_generator)
        value = " ".join(await _words_gen.run())
        logger.debug("value: %r.", value)
        return value
