__all__ = (
    "RandomValueGeneratorInterface",
    "BaseRandCollectionGenerator",
)

import logging
import typing as t

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


ValueTypeVar = t.TypeVar("ValueTypeVar")


class RandomValueGeneratorInterface(t.Generic[ValueTypeVar]):
    def run(self) -> ValueTypeVar:
        raise NotImplementedError(f"{self.__class__}.run")


class BaseRandCollectionGenerator(
    RandomValueGeneratorInterface[ValueTypeVar], t.Generic[ValueTypeVar]
):

    def __init__(self, len: t.Union[int, "RandomValueGeneratorInterface[int]"]):
        self._len = len

    def _get_rand_len(self) -> int:
        if isinstance(self._len, int):
            return self._len
        return self._len.run()
