__all__ = (
    "AsyncRandList",
    "AsyncRandSet",
    "AsyncRandDict",
    "AsyncRandValuesDict",
    "BaseAsyncRandCollectionGenerator",
)

import asyncio
import logging
import typing as t

from .base import (
    AsyncRandomValueBuilderInterface,
    BaseAsyncRandCollectionGenerator,
)

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


ValueTypeVar = t.TypeVar("ValueTypeVar")


class AsyncRandList(
    BaseAsyncRandCollectionGenerator[list[ValueTypeVar]],
    t.Generic[ValueTypeVar],
):
    def __init__(
        self, item: "AsyncRandomValueBuilderInterface[ValueTypeVar]", **kwargs
    ):
        super().__init__(**kwargs)
        self._item_generator = item

    async def run(self) -> list[ValueTypeVar]:
        _len = await self._get_rand_len()
        value = []
        for _ in range(_len):
            value.append(await self._item_generator.run())
            await asyncio.sleep(0)
        logger.debug("value: %r.", value)
        return value


class AsyncRandSet(
    BaseAsyncRandCollectionGenerator[set[ValueTypeVar]], t.Generic[ValueTypeVar]
):
    def __init__(
        self, item: "AsyncRandomValueBuilderInterface[ValueTypeVar]", **kwargs
    ):
        super().__init__(**kwargs)
        self._item_generator = item

    async def run(self) -> set[ValueTypeVar]:
        _len = await self._get_rand_len()
        value = set()
        for _ in range(_len):
            value.add(await self._item_generator.run())
            await asyncio.sleep(0)
        logger.debug("value: %r.", value)
        return value


KeyTypeVar = t.TypeVar("KeyTypeVar")


class AsyncRandDict(
    BaseAsyncRandCollectionGenerator[dict[KeyTypeVar, ValueTypeVar]],
    t.Generic[KeyTypeVar, ValueTypeVar],
):
    def __init__(
        self,
        key: "AsyncRandomValueBuilderInterface[KeyTypeVar]",
        value: "AsyncRandomValueBuilderInterface[ValueTypeVar]",
        **kwargs: "AsyncRandomValueBuilderInterface",
    ):
        super().__init__(**kwargs)
        self._key_generator = key
        self._value_generator = value

    async def run(self) -> dict[KeyTypeVar, ValueTypeVar]:
        _len = await self._get_rand_len()
        value = {}
        for _ in range(_len):
            k = await self._key_generator.run()
            v = await self._value_generator.run()
            value[k] = v
            await asyncio.sleep(0)
        logger.debug("value: %r.", value)
        return value


class AsyncRandValuesDict(AsyncRandomValueBuilderInterface[dict[str, t.Any]]):

    def __init__(self, **kwargs: "AsyncRandomValueBuilderInterface"):
        self._keys_generators = kwargs

    async def run(self) -> dict[str, t.Any]:
        value = {k: await g.run() for k, g in self._keys_generators.items()}
        logger.debug("value: %r.", value)
        return value
