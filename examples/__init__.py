import logging
import typing as t
from dataclasses import dataclass
from datetime import datetime

from random_fish import (
    RandBool,
    RandDataclass,
    RandDateTime,
    RandDict,
    RandFloat,
    RandInt,
    RandList,
    RandSet,
    RandString,
    RandTuple,
    RandValuesDict,
)

if t.TYPE_CHECKING:
    ...

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


rb = RandBool()
ri = RandInt(min=10, max=100)
rf = RandFloat(min=2.0, max=8.0)
rs = RandString(len=50)
rt = RandTuple[tuple[bool, int, float, str]](rb, ri, rf, rs)

for _ in range(10):
    print(rb.run(), ri.run(), rf.run(), rs.run(), rt.run())

rli = RandList[int](len=10, item=RandInt(min=200, max=300))
print(rli.run())

rls = RandList[str](
    len=RandInt(min=5, max=10), item=RandString(len=RandInt(min=10, max=30))
)
print(rls.run())

rsf = RandSet[float](len=20, item=RandFloat(min=50, max=100))
print(rsf.run())

rdsi = RandDict[str, int](
    len=RandInt(min=5, max=10),
    key=RandString(len=RandInt(min=5, max=10)),
    value=RandInt(min=1000, max=2000),
)
print(rdsi.run())

rdv = RandValuesDict(
    key_bool=rb,
    key_int=ri,
    key_float=rf,
    key_str=rs,
    key_list_int=rli,
    key_list_str=rls,
    key_dict_str_int=rdsi,
)
for k, v in rdv.run().items():
    print(f"{k}: {v}")


@dataclass
class DemoDataclass:
    f_bool: bool
    f_int: int
    f_float: float
    f_str: str


rc = RandDataclass(
    cls=DemoDataclass,
    f_bool=rb,
    f_int=ri,
    f_float=rf,
    f_str=rs,
)
print(rc.run())

rdt = RandDateTime(
    min=datetime(year=2024, month=1, day=1),
    max=datetime(year=2025, month=1, day=1),
)
for _ in range(100):
    print(rdt.run())
