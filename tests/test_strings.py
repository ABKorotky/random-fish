import typing as t

from random_fish.choice import RandomChoice
from random_fish.strings import (
    RandomString,
    RandomTemplatedString,
    RandomText,
    RandomWord,
)
from tests.helpers import ClassTestingHelper

if t.TYPE_CHECKING:
    ...


class RandomStringTestCase(ClassTestingHelper[RandomString]):
    tst_cls = RandomString
    len: int = 5
    chars: str = "abcde"

    def setUp(self):
        self.tst_obj = self.build_tst_obj(len=self.len, chars=self.chars)

    def test_next(self):
        tst_res = next(self.tst_obj)
        assert len(tst_res) == self.len
        for i in tst_res:
            assert i in self.chars

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        assert len(tst_res) == self.len
        for i in tst_res:
            assert i in self.chars


class RandomWordTestCase(ClassTestingHelper[RandomWord]):
    tst_cls = RandomWord
    len: int = 5

    def setUp(self):
        self.tst_obj = self.build_tst_obj(len=self.len)

    def test_next(self):
        tst_res = next(self.tst_obj)
        assert len(tst_res) == self.len

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        assert len(tst_res) == self.len


class RandomTemplatedStringTestCase(ClassTestingHelper[RandomTemplatedString]):
    tst_cls = RandomTemplatedString
    template: str = "{0}@mail.com"
    names: str = (
        "adam",
        "bob",
        "charlie",
    )
    all_templates: list[str]

    @classmethod
    def setUpClass(cls):
        cls.all_templates = [cls.template.format(i) for i in cls.names]

    def setUp(self):
        self.tst_obj = self.build_tst_obj(
            self.template, RandomChoice(*self.names)
        )

    def test_next(self):
        tst_res = next(self.tst_obj)
        assert tst_res in self.all_templates

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        assert tst_res in self.all_templates


class RandomTextTestCase(ClassTestingHelper[RandomText]):
    tst_cls = RandomText
    len: int = 4
    word_len: int = 5

    def setUp(self):
        word_fish = RandomWord(len=self.word_len)
        self.tst_obj = self.build_tst_obj(len=self.len, word=word_fish)

    def test_next(self):
        tst_res = next(self.tst_obj)
        words = tst_res.split()
        assert len(words) == self.len
        for word in words:
            assert len(word) == self.word_len

    async def test_anext(self):
        tst_res = await anext(self.tst_obj)
        words = tst_res.split()
        assert len(words) == self.len
        for word in words:
            assert len(word) == self.word_len
