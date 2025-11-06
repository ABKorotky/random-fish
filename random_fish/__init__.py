"""Random Fish.

Generates different random objects according to different strategies.
"""

__all__ = (
    "NAME",
    "VERSION",
    "PY_VERSION",
    "AUTHOR",
    "AUTHOR_EMAIL",
    "RandomValueBuilderInterface",
    "RandBool",
    "RandInt",
    "RandFloat",
    "RandString",
    "RandText",
    "RandTuple",
    "RandChoice",
    "RandIntChoice",
    "RandSequenceGenerator",
    "LengthType",
    "RandList",
    "RandSet",
    "RandDict",
    "RandValuesDict",
    "RandDataclass",
    "RandDateTime",
)

from random_fish.base import RandomValueBuilderInterface
from random_fish.choice import RandChoice, RandIntChoice
from random_fish.classes import RandDataclass
from random_fish.collections import (
    LengthType,
    RandDict,
    RandList,
    RandSequenceGenerator,
    RandSet,
    RandValuesDict,
)
from random_fish.datetimes import RandDateTime
from random_fish.scalar import RandBool, RandFloat, RandInt, RandTuple
from random_fish.strings import RandString, RandText

NAME = "random-fish"
TITLE = "Random Fish"
DESCRIPTION = (
    "Generates different random objects according to different strategies"
)

VERSION = (
    0,
    1,
    0,
)
PY_VERSION = (
    3,
    13,
)

AUTHOR = "Aliaksandr Karotki"
AUTHOR_EMAIL = "abkorotky@gmail.com"
