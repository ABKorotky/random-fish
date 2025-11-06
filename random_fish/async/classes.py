__all__ = ("AsyncRandDataclass",)

import logging
import typing as t

from .base import AsyncRandomValueBuilderInterface

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


ValueTypeVar = t.TypeVar("ValueTypeVar")


class AsyncRandDataclass(
    AsyncRandomValueBuilderInterface[ValueTypeVar], t.Generic[ValueTypeVar]
):
    def __init__(
        self,
        cls: type[ValueTypeVar],
        **kwargs: "AsyncRandomValueBuilderInterface",
    ):
        self._dataclass_cls = cls
        self._fields_generators = kwargs

    async def run(self) -> ValueTypeVar:
        fields = {f: await g.run() for f, g in self._fields_generators.items()}
        value = self._dataclass_cls(**fields)
        logger.debug("value: %r.", value)
        return value
