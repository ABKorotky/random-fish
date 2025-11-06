__all__ = (
    "AsyncRandomValueGeneratorInterface",
    "BaseAsyncRandCollectionGenerator",
)

import logging
import typing as t

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


ValueTypeVar = t.TypeVar("ValueTypeVar")


class AsyncRandomValueGeneratorInterface(t.Generic[ValueTypeVar]):
    async def run(self) -> ValueTypeVar:
        raise NotImplementedError(f"{self.__class__}.run")


class BaseAsyncRandCollectionGenerator(
    AsyncRandomValueGeneratorInterface[ValueTypeVar], t.Generic[ValueTypeVar]
):

    def __init__(
        self, len: t.Union[int, "AsyncRandomValueGeneratorInterface[int]"]
    ):
        self._len = len

    async def _get_rand_len(self) -> int:
        if isinstance(self._len, int):
            return self._len
        return await self._len.run()
