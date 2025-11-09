import typing as t
from dataclasses import dataclass

from random_fish.scalar import RandomFloat, RandomInt
from random_fish.structural import RandomDataclass, RandomDict, RandomTuple
from tests.helpers import ClassTestingHelper

if t.TYPE_CHECKING:
    ...


class RandomTupleTestCase(ClassTestingHelper[RandomTuple[tuple[int, float]]]):
    tst_cls = RandomTuple
    min1: int = 1
    max1: int = 10
    min2: int = 0.0
    max2: int = 1.0

    def setUp(self):
        self.tst_obj = self.build_tst_obj(
            RandomInt(self.min1, self.max1),
            RandomFloat(self.min2, self.max2),
        )

    def test_next(self):
        tst_res = next(self.tst_obj)
        assert self.min1 <= tst_res[0] <= self.max1
        assert self.min2 <= tst_res[1] <= self.max2

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        assert self.min1 <= tst_res[0] <= self.max1
        assert self.min2 <= tst_res[1] <= self.max2


@dataclass
class TstDataclass:
    name: str
    age: int


class RandomDataclassTestCase(
    ClassTestingHelper[RandomDataclass[TstDataclass]]
):
    tst_cls = RandomDataclass
    names = ("adam", "bob", "charlie")
    min: int = 18
    max: int = 99

    def setUp(self):
        from random_fish import RandomChoice

        self.tst_obj = self.build_tst_obj(
            TstDataclass,
            name=RandomChoice(*self.names),
            age=RandomInt(self.min, self.max),
        )

    def test_next(self):
        tst_res = next(self.tst_obj)
        assert tst_res.name in self.names
        assert self.min <= tst_res.age <= self.max

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        assert tst_res.name in self.names
        assert self.min <= tst_res.age <= self.max


class RandomDictTestCase(ClassTestingHelper[RandomDict]):
    tst_cls = RandomDict
    names = ("adam", "bob", "charlie")
    min: int = 18
    max: int = 99

    def setUp(self):
        from random_fish import RandomChoice

        self.tst_obj = self.build_tst_obj(
            name=RandomChoice(*self.names),
            age=RandomInt(self.min, self.max),
        )

    def test_next(self):
        tst_res = next(self.tst_obj)
        assert tst_res["name"] in self.names
        assert self.min <= tst_res["age"] <= self.max

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        assert tst_res["name"] in self.names
        assert self.min <= tst_res["age"] <= self.max
