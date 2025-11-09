import datetime
import typing as t

from random_fish.datetime import RandomDateTime
from tests.helpers import ClassTestingHelper

if t.TYPE_CHECKING:
    ...


class RandomDateTimeTestCase(ClassTestingHelper[RandomDateTime]):
    tst_cls = RandomDateTime
    min = datetime.datetime(2023, 1, 1)
    max = datetime.datetime(2023, 1, 10)

    def setUp(self):
        self.tst_obj = self.build_tst_obj(self.min, self.max)

    def test_next(self):
        tst_res = next(self.tst_obj)
        assert self.min <= tst_res <= self.max

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        assert self.min <= tst_res <= self.max
