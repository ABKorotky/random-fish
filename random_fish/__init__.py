"""Random Fish.

Generates different random objects according to different strategies.
"""

__all__ = (
    "NAME",
    "TITLE",
    "DESCRIPTION",
    "VERSION",
    "PY_VERSION",
    "AUTHOR",
    "AUTHOR_EMAIL",
    "RandomBool",
    "RandomFloat",
    "RandomInt",
    "RandomDateTime",
    "RandomChoice",
    "RandomEnumChoice",
    "RandomString",
    "RandomWord",
    "RandomTemplatedString",
    "RandomText",
    "RandomTuple",
    "RandomDict",
    "RandomDataclass",
    "RandomFishIterator",
    "RandomList",
    "RandomSet",
    "RandomMap",
)

from random_fish.choice import RandomChoice, RandomEnumChoice
from random_fish.collections import RandomList, RandomMap, RandomSet
from random_fish.datetime import RandomDateTime
from random_fish.iterators import RandomFishIterator
from random_fish.scalar import RandomBool, RandomFloat, RandomInt
from random_fish.strings import (
    RandomString,
    RandomTemplatedString,
    RandomText,
    RandomWord,
)
from random_fish.structural import (
    RandomDataclass,
    RandomDict,
    RandomTuple,
)

NAME = "random-fish"
TITLE = "Random Fish"
DESCRIPTION = (
    "Generates different random objects according to different strategies"
)

VERSION = (
    0,
    2,
    0,
)
PY_VERSION = (
    3,
    13,
)

AUTHOR = "Aliaksandr Karotki"
AUTHOR_EMAIL = "abkorotky@gmail.com"
