__all__ = (
    "RandomFishInterface",
    "RandomSchoolOfFishInterface",
)

import typing as t

if t.TYPE_CHECKING:
    ...


ValueTypeVar = t.TypeVar("ValueTypeVar")


class RandomFishInterface(t.Generic[ValueTypeVar]):

    def __next__(self) -> ValueTypeVar:
        raise NotImplementedError(f"{self.__class__}.__next__")

    async def __anext__(self) -> ValueTypeVar:
        raise NotImplementedError(f"{self.__class__}.__anext__")


ItemTypeVar = t.TypeVar("ItemTypeVar")


class RandomSchoolOfFishInterface(t.Generic[ItemTypeVar]):
    def __iter__(self) -> t.Iterator[ItemTypeVar]:
        raise NotImplementedError(f"{self.__class__}.__iter__")

    def __aiter__(self) -> t.AsyncIterator[ItemTypeVar]:
        raise NotImplementedError(f"{self.__class__}.__aiter__")
