__all__ = ("RandomValueBuilderInterface",)

import logging
import typing as t

if t.TYPE_CHECKING:
    ...

logger = logging.getLogger(__name__)

ValueTypeVar = t.TypeVar("ValueTypeVar")


class RandomValueBuilderInterface(t.Generic[ValueTypeVar]):
    def run(self) -> ValueTypeVar:
        raise NotImplementedError(f"{self.__class__}.run")
