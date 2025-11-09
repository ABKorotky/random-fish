import typing as t
from enum import Enum

from random_fish.choice import RandomChoice, RandomEnumChoice
from tests.helpers import ClassTestingHelper

if t.TYPE_CHECKING:
    ...


class RandomChoiceTestCase(ClassTestingHelper[RandomChoice]):
    tst_cls = RandomChoice

    def setUp(self):
        self.tst_obj = self.build_tst_obj(1, 2, 3)

    def test_next(self):
        self.assertIn(next(self.tst_obj), (1, 2, 3))

    async def test_anext(self):
        self.assertIn(await anext(self.tst_obj), (1, 2, 3))


class TstEnum(Enum):
    A = 1
    B = 2
    C = 3


class RandomEnumChoiceTestCase(ClassTestingHelper[RandomEnumChoice]):
    tst_cls = RandomEnumChoice

    @classmethod
    def setUpClass(cls) -> None:
        cls.tst_obj = cls.build_tst_obj(TstEnum)

    def test_next(self):
        self.assertIn(next(self.tst_obj), TstEnum)

    async def test_anext(self):
        self.assertIn(await anext(self.tst_obj), TstEnum)
