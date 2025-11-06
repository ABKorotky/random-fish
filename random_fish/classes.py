__all__ = ("RandDataclass",)

import logging
import typing as t

from .base import RandomValueGeneratorInterface

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)


ValueTypeVar = t.TypeVar("ValueTypeVar")


class RandDataclass(
    RandomValueGeneratorInterface[ValueTypeVar], t.Generic[ValueTypeVar]
):
    def __init__(
        self, cls: type[ValueTypeVar], **kwargs: "RandomValueGeneratorInterface"
    ):
        self._dataclass_cls = cls
        self._fields_generators = kwargs

    def run(self) -> ValueTypeVar:
        fields = {f: g.run() for f, g in self._fields_generators.items()}
        value = self._dataclass_cls(**fields)
        logger.debug("Random generator: %r. Value: %r.", self, value)
        return value
