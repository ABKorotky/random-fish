__all__ = (
    "RandList",
    "RandSet",
    "RandDict",
    "RandValuesDict",
)

import logging
import typing as t

from .base import BaseRandCollectionGenerator, RandomValueGeneratorInterface

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


ValueTypeVar = t.TypeVar("ValueTypeVar")


class RandList(
    BaseRandCollectionGenerator[list[ValueTypeVar]], t.Generic[ValueTypeVar]
):
    def __init__(
        self, item: "RandomValueGeneratorInterface[ValueTypeVar]", **kwargs
    ):
        super().__init__(**kwargs)
        self._item_generator = item

    def run(self) -> list[ValueTypeVar]:
        value = [
            self._item_generator.run() for _ in range(self._get_rand_len())
        ]
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value


class RandSet(
    BaseRandCollectionGenerator[set[ValueTypeVar]], t.Generic[ValueTypeVar]
):
    def __init__(
        self, item: "RandomValueGeneratorInterface[ValueTypeVar]", **kwargs
    ):
        super().__init__(**kwargs)
        self._item_generator = item

    def run(self) -> set[ValueTypeVar]:
        value = {
            self._item_generator.run() for _ in range(self._get_rand_len())
        }
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value


KeyTypeVar = t.TypeVar("KeyTypeVar")


class RandDict(
    BaseRandCollectionGenerator[dict[KeyTypeVar, ValueTypeVar]],
    t.Generic[KeyTypeVar, ValueTypeVar],
):
    def __init__(
        self,
        key: "RandomValueGeneratorInterface[KeyTypeVar]",
        value: "RandomValueGeneratorInterface[ValueTypeVar]",
        **kwargs: "RandomValueGeneratorInterface",
    ):
        super().__init__(**kwargs)
        self._key_generator = key
        self._value_generator = value

    def run(self) -> dict[KeyTypeVar, ValueTypeVar]:
        value = {
            self._key_generator.run(): self._value_generator.run()
            for _ in range(self._get_rand_len())
        }
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value


class RandValuesDict(RandomValueGeneratorInterface[dict[str, t.Any]]):

    def __init__(self, **kwargs: "RandomValueGeneratorInterface"):
        self._keys_generators = kwargs

    def run(self) -> dict[str, t.Any]:
        value = {k: g.run() for k, g in self._keys_generators.items()}
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value
