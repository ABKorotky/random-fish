__all__ = (
    "RandSequenceGenerator",
    "LengthType",
    "RandList",
    "RandSet",
    "RandDict",
    "RandValuesDict",
)

import logging
import typing as t

from .base import RandomValueBuilderInterface
from .scalar import RandTuple

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


LengthType = t.Union[int, "RandomValueBuilderInterface[int]"]
ValueTypeVar = t.TypeVar("ValueTypeVar")


class RandSequenceGenerator(
    RandomValueBuilderInterface[ValueTypeVar],
    t.Generic[ValueTypeVar],
):
    def __init__(
        self,
        len: "LengthType",
        item: "RandomValueBuilderInterface[ValueTypeVar]",
    ):
        self._len = len
        self._item_builder = item

    def run(self) -> t.Iterator[ValueTypeVar]:
        _len = self._get_rand_len()
        for i in range(_len):
            value = self._item_builder.run()
            logger.debug("iteration: %r. value: %r.", i, value)
            yield value

    def _get_rand_len(self) -> int:
        if isinstance(self._len, int):
            return self._len
        return self._len.run()


class RandList(
    RandomValueBuilderInterface[list[ValueTypeVar]], t.Generic[ValueTypeVar]
):
    def __init__(
        self,
        len: "LengthType",
        item: "RandomValueBuilderInterface[ValueTypeVar]",
    ):
        self._gen = RandSequenceGenerator(len=len, item=item)

    def run(self) -> list[ValueTypeVar]:
        value = [item for item in self._gen.run()]
        logger.debug("value: %r.", value)
        return value


class RandSet(
    RandomValueBuilderInterface[set[ValueTypeVar]], t.Generic[ValueTypeVar]
):
    def __init__(
        self,
        len: "LengthType",
        item: "RandomValueBuilderInterface[ValueTypeVar]",
    ):
        self._gen = RandSequenceGenerator(len=len, item=item)

    def run(self) -> set[ValueTypeVar]:
        value = {item for item in self._gen.run()}
        logger.debug("value: %r.", value)
        return value


KeyTypeVar = t.TypeVar("KeyTypeVar")


class RandDict(
    RandomValueBuilderInterface[dict[KeyTypeVar, ValueTypeVar]],
    t.Generic[KeyTypeVar, ValueTypeVar],
):
    def __init__(
        self,
        len: "LengthType",
        key: "RandomValueBuilderInterface[KeyTypeVar]",
        value: "RandomValueBuilderInterface[ValueTypeVar]",
    ):
        self._gen = RandSequenceGenerator(len=len, item=RandTuple(key, value))

    def run(self) -> dict[KeyTypeVar, ValueTypeVar]:
        value = {k: v for k, v in self._gen.run()}
        logger.debug("value: %r.", value)
        return value


class RandValuesDict(RandomValueBuilderInterface[dict[str, t.Any]]):

    def __init__(self, **kwargs: "RandomValueBuilderInterface"):
        self._keys_builders = kwargs

    def run(self) -> dict[str, t.Any]:
        value = {
            key: builder.run() for key, builder in self._keys_builders.items()
        }
        logger.debug("value: %r.", value)
        return value
