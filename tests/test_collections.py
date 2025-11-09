import typing as t

from random_fish.collections import RandomList, RandomMap, RandomSet
from random_fish.scalar import RandomInt
from tests.helpers import ClassTestingHelper

if t.TYPE_CHECKING:
    ...


class RandomListTestCase(ClassTestingHelper[RandomList[int]]):
    tst_cls = RandomList
    len: int = 5
    min: int = 1
    max: int = 10

    def setUp(self) -> None:
        self.tst_obj = self.build_tst_obj(
            len=self.len, item=RandomInt(self.min, self.max)
        )

    def test_next(self):
        tst_res = next(self.tst_obj)
        assert len(tst_res) == self.len
        for i in tst_res:
            assert self.min <= i <= self.max

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        assert len(tst_res) == self.len
        for i in tst_res:
            assert self.min <= i <= self.max

    def test_iter(self):
        counter = 0
        for i in self.tst_obj:
            counter += 1
            assert self.min <= i <= self.max
        assert counter == self.len

    async def test_aiter(self):
        counter = 0
        async for i in self.tst_obj:
            counter += 1
            assert self.min <= i <= self.max
        assert counter == self.len


class RandomSetTestCase(ClassTestingHelper[RandomSet[int]]):
    tst_cls = RandomSet
    len: int = 5
    min: int = 1
    max: int = 10

    def setUp(self) -> None:
        self.tst_obj = self.build_tst_obj(
            len=self.len, item=RandomInt(self.min, self.max)
        )

    def test_next(self):
        tst_res = next(self.tst_obj)
        assert len(tst_res) <= self.len
        for i in tst_res:
            assert self.min <= i <= self.max

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        assert len(tst_res) <= self.len
        for i in tst_res:
            assert self.min <= i <= self.max

    def test_iter(self):
        counter = 0
        for i in self.tst_obj:
            counter += 1
            assert self.min <= i <= self.max
        assert counter <= self.len

    async def test_aiter(self):
        counter = 0
        async for i in self.tst_obj:
            counter += 1
            assert self.min <= i <= self.max
        assert counter <= self.len


class RandomMapTestCase(ClassTestingHelper[RandomMap[int, int]]):
    tst_cls = RandomMap
    len: int = 5
    min: int = 1
    max: int = 10

    def setUp(self) -> None:
        self.tst_obj = self.build_tst_obj(
            len=self.len,
            key=RandomInt(self.min, self.max),
            value=RandomInt(self.min, self.max),
        )

    def test_next(self):
        tst_res = next(self.tst_obj)
        assert len(tst_res) <= self.len
        for k, v in tst_res.items():
            assert self.min <= k <= self.max
            assert self.min <= v <= self.max

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        assert len(tst_res) <= self.len
        for k, v in tst_res.items():
            assert self.min <= k <= self.max
            assert self.min <= v <= self.max

    def test_iter(self):
        counter = 0
        for k, v in self.tst_obj:
            counter += 1
            assert self.min <= k <= self.max
            assert self.min <= v <= self.max
        assert counter <= self.len

    async def test_aiter(self):
        counter = 0
        async for k, v in self.tst_obj:
            counter += 1
            assert self.min <= k <= self.max
            assert self.min <= v <= self.max
        assert counter <= self.len
