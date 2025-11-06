__all__ = (
    "AsyncRandomValueBuilderInterface",
    "BaseAsyncRandCollectionGenerator",
)

import logging
import typing as t

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


ValueTypeVar = t.TypeVar("ValueTypeVar")


class AsyncRandomValueBuilderInterface(t.Generic[ValueTypeVar]):
    async def run(self) -> ValueTypeVar:
        raise NotImplementedError(f"{self.__class__}.run")


class BaseAsyncRandCollectionGenerator(
    AsyncRandomValueBuilderInterface[ValueTypeVar], t.Generic[ValueTypeVar]
):

    def __init__(
        self, len: t.Union[int, "AsyncRandomValueBuilderInterface[int]"]
    ):
        self._len = len

    async def _get_rand_len(self) -> int:
        if isinstance(self._len, int):
            return self._len
        return await self._len.run()
