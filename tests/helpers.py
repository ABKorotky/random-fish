__all__ = ("ClassTestingHelper",)

import typing as t
from unittest import IsolatedAsyncioTestCase

if t.TYPE_CHECKING:
    ...


TestedClassTypeVar = t.TypeVar("TestedClassTypeVar")


class ClassTestingHelper(
    IsolatedAsyncioTestCase, t.Generic[TestedClassTypeVar]
):
    tst_cls: type[TestedClassTypeVar]
    tst_obj: TestedClassTypeVar

    @classmethod
    def build_tst_obj(
        cls,
        *args,
        tst_cls: t.Optional[type[TestedClassTypeVar]] = None,
        **kwargs,
    ) -> TestedClassTypeVar:
        tst_cls = tst_cls or cls.tst_cls
        return tst_cls(*args, **kwargs)
