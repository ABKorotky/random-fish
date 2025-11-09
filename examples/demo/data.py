__all__ = (
    "NAMES",
    "SURNAMES",
    "Gender",
    "Address",
    "Person",
)

import typing as t
from dataclasses import dataclass
from enum import Enum

if t.TYPE_CHECKING:
    ...


NAMES = ["John", "Jane", "Mary", "Alice", "Bob"]
SURNAMES = ["Doe", "Smith", "Johnson", "Brown", "Williams"]


class Gender(Enum):
    MALE = 1
    FEMALE = 2


@dataclass
class Address:
    flat: int
    house: str
    street: str
    city: str
    zip_code: str


@dataclass
class Person:
    name: str
    surname: str
    age: int
    gender: Gender
    address: Address
    tags: list[str]
    attributes: dict[str, dict]
