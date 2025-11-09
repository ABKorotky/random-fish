__all__ = (
    "RandomTuple",
    "RandomDict",
    "RandomDataclass",
)

import logging
import typing as t

from random_fish.base import RandomFishInterface

if t.TYPE_CHECKING:
    ...


logger = logging.getLogger(__name__)


TupleTypeVar = t.TypeVar("TupleTypeVar", bound=tuple)


class RandomTuple(RandomFishInterface[TupleTypeVar], t.Generic[TupleTypeVar]):
    def __init__(self, *args: RandomFishInterface):
        self._fishes = args

    def __next__(self) -> TupleTypeVar:
        val = tuple([next(fish) for fish in self._fishes])
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val  # type: ignore[return-value]

    async def __anext__(self) -> TupleTypeVar:
        val = tuple([await anext(fish) for fish in self._fishes])
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val  # type: ignore[return-value]


StructureTypeVar = t.TypeVar("StructureTypeVar")


class BaseRandomStructure(
    RandomFishInterface[StructureTypeVar], t.Generic[StructureTypeVar]
):
    def __init__(self, **kwargs: RandomFishInterface):
        self._named_fishes = kwargs


class RandomDict(BaseRandomStructure[dict[str, t.Any]]):
    def __next__(self) -> dict[str, t.Any]:
        val = {name: next(fish) for name, fish in self._named_fishes.items()}
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    async def __anext__(self) -> dict[str, t.Any]:
        val = {
            name: await anext(fish) for name, fish in self._named_fishes.items()
        }
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val


DataclassTypeVar = t.TypeVar("DataclassTypeVar")


class RandomDataclass(
    BaseRandomStructure[DataclassTypeVar], t.Generic[DataclassTypeVar]
):

    def __init__(self, dataclass_type: type[DataclassTypeVar], **kwargs):
        super().__init__(**kwargs)
        self._cls = dataclass_type

    def __next__(self) -> DataclassTypeVar:
        fields = {name: next(fish) for name, fish in self._named_fishes.items()}
        val = self._cls(**fields)
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val

    async def __anext__(self) -> DataclassTypeVar:
        fields = {
            name: await anext(fish) for name, fish in self._named_fishes.items()
        }
        val = self._cls(**fields)
        if __debug__:
            logger.debug("instance: %r. value: %r.", self, val)
        return val
