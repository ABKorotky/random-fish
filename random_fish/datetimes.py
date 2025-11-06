__all__ = ("RandDateTime",)

import logging
import typing as t
from datetime import datetime
from random import randint

from .base import RandomValueBuilderInterface

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


ValueTypeVar = t.TypeVar("ValueTypeVar")


class RandDateTime(RandomValueBuilderInterface["datetime"]):
    def __init__(self, min: "datetime", max: "datetime"):
        self._min_timestamp = int(min.timestamp())
        self._max_timestamp = int(max.timestamp())

    def run(self) -> "datetime":
        value = datetime.fromtimestamp(
            randint(self._min_timestamp, self._max_timestamp)
        )
        logger.debug("value: %r.", value)
        return value
