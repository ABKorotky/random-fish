__all__ = ("RandDataclass",)

import logging
import typing as t

from .base import RandomValueBuilderInterface

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


ValueTypeVar = t.TypeVar("ValueTypeVar")


class RandDataclass(
    RandomValueBuilderInterface[ValueTypeVar], t.Generic[ValueTypeVar]
):
    def __init__(
        self, cls: type[ValueTypeVar], **kwargs: "RandomValueBuilderInterface"
    ):
        self._dataclass_cls = cls
        self._fields_builders = kwargs

    def run(self) -> ValueTypeVar:
        fields = {
            name: builder.run()
            for name, builder in self._fields_builders.items()
        }
        value = self._dataclass_cls(**fields)
        logger.debug("value: %r.", value)
        return value
