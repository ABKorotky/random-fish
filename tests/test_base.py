import typing as t

from random_fish.base import RandomFishInterface, RandomSchoolOfFishInterface
from tests.helpers import ClassTestingHelper

if t.TYPE_CHECKING:
    ...


class RandomFishInterfaceTestCase(ClassTestingHelper[RandomFishInterface]):
    tst_cls = RandomFishInterface

    @classmethod
    def setUpClass(cls) -> None:
        cls.tst_obj = cls.build_tst_obj()

    def test_next(self):
        with self.assertRaises(NotImplementedError):
            next(self.tst_obj)

    async def test_anext(self):
        with self.assertRaises(NotImplementedError):
            await anext(self.tst_obj)


class RandomSchoolOfFishInterfaceTestCase(
    ClassTestingHelper[RandomSchoolOfFishInterface]
):
    tst_cls = RandomSchoolOfFishInterface

    @classmethod
    def setUpClass(cls) -> None:
        cls.tst_obj = cls.build_tst_obj()

    def test_iter(self):
        with self.assertRaises(NotImplementedError):
            iter(self.tst_obj)

    async def test_aiter(self):
        with self.assertRaises(NotImplementedError):
            async for _ in self.tst_obj:
                pass
