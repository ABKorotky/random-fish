import typing as t

from random_fish.iterators import RandomFishIterator
from random_fish.scalar import RandomInt
from random_fish.structural import RandomTuple
from tests.helpers import ClassTestingHelper

if t.TYPE_CHECKING:
    ...


class RandomListTestCase(
    ClassTestingHelper[RandomFishIterator[tuple[int, int]]]
):
    tst_cls = RandomFishIterator
    min_len: int = 5
    max_len: int = 10
    min1: int = 11
    max1: int = 20
    min2: int = 21
    max2: int = 30

    def setUp(self) -> None:
        self.tst_obj = self.build_tst_obj(
            item=RandomTuple(
                RandomInt(self.min1, self.max1),
                RandomInt(self.min2, self.max2),
            ),
            len=RandomInt(self.min_len, self.max_len),
        )

    def test_iter(self):
        counter = 0
        for i1, i2 in self.tst_obj:
            counter += 1
            assert self.min1 <= i1 <= self.max1
            assert self.min2 <= i2 <= self.max2
        assert self.min_len <= counter <= self.max_len

    async def test_aiter(self):
        counter = 0
        async for i1, i2 in self.tst_obj:
            counter += 1
            assert self.min1 <= i1 <= self.max1
            assert self.min2 <= i2 <= self.max2
        assert self.min_len <= counter <= self.max_len
