import typing as t

from random_fish.scalar import RandomBool, RandomFloat, RandomInt
from tests.helpers import ClassTestingHelper

if t.TYPE_CHECKING:
    ...


class RandomBoolTestCase(ClassTestingHelper[RandomBool]):
    tst_cls = RandomBool

    def setUp(self):
        self.tst_obj = self.build_tst_obj()

    def test_next(self):
        self.assertIn(next(self.tst_obj), (True, False))

    async def test_anext(self):
        self.assertIn(await anext(self.tst_obj), (True, False))


class RandomIntTestCase(ClassTestingHelper[RandomInt]):
    tst_cls = RandomInt
    min: int = 1
    max: int = 10

    def setUp(self):
        self.tst_obj = self.build_tst_obj(self.min, self.max)

    def test_next(self):
        tst_res = next(self.tst_obj)
        assert self.min <= tst_res <= self.max

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        assert self.min <= tst_res <= self.max


class RandomFloatTestCase(ClassTestingHelper[RandomFloat]):
    tst_cls = RandomFloat
    min: float = 0.0
    max: float = 1.0

    def setUp(self):
        self.tst_obj = self.build_tst_obj(self.min, self.max)

    def test_next(self):
        tst_res = next(self.tst_obj)
        assert self.min <= tst_res <= self.max

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        assert self.min <= tst_res <= self.max
