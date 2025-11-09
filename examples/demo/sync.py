# flake8: noqa: E402
import os
import sys
import typing as t

sys.path.append(os.curdir)

from examples.demo.data import NAMES, SURNAMES, Address, Gender, Person
from random_fish import (
    RandomBool,
    RandomChoice,
    RandomDataclass,
    RandomDict,
    RandomEnumChoice,
    RandomFloat,
    RandomInt,
    RandomList,
    RandomMap,
    RandomWord,
)

if t.TYPE_CHECKING:
    ...


def main():
    random_person = RandomDataclass(
        dataclass_type=Person,
        name=RandomChoice(*NAMES),
        surname=RandomChoice(*SURNAMES),
        age=RandomInt(min=0, max=100),
        gender=RandomEnumChoice(Gender),
        address=RandomDataclass(
            dataclass_type=Address,
            flat=RandomInt(min=1, max=100),
            house=RandomInt(min=1, max=100),
            street=RandomChoice(*NAMES),
            city=RandomChoice(*NAMES),
            zip_code=RandomInt(min=1000, max=9999),
        ),
        tags=RandomList(
            len=RandomInt(min=1, max=3),
            item=RandomChoice(
                *["friend", "colleague", "family", "acquaintance"]
            ),
        ),
        attributes=RandomMap(
            len=RandomInt(min=1, max=3),
            key=RandomWord(len=RandomInt(min=5, max=10)),
            value=RandomDict(
                name=RandomWord(len=RandomInt(min=5, max=10)),
                type=RandomWord(len=RandomInt(min=5, max=10)),
                is_enabled=RandomBool(),
                weight=RandomFloat(min=0.0, max=100.0),
            ),
        ),
    )
    persons = RandomList(len=RandomInt(min=10, max=20), item=random_person)
    for person in persons:
        print(person)


if __name__ == "__main__":
    main()
