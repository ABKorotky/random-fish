# flake8: noqa: E402

import asyncio
import logging
import os
import sys
import typing as t

sys.path.append(os.curdir)

from examples.performance.helpers import PerfTimer
from random_fish import (
    RandomBool,
    RandomFishIterator,
    RandomFloat,
    RandomInt,
    RandomList,
    RandomTuple,
)

if t.TYPE_CHECKING:
    from random_fish.base import RandomFishInterface

    from .helpers import PerfInfo


logging.basicConfig(level=logging.INFO)


async def measure_range_next(n: int, fish: "RandomFishInterface") -> "PerfInfo":
    timer = PerfTimer()
    with timer:
        # list([await anext(fish) for _i in range(n)])
        for _i in range(n):
            await anext(fish)

    if __debug__:
        logging.debug("iter. %r. iterations: %r. %r.", fish, n, timer)
    return timer.get_info()


async def measure_random_iterator(
    n: int, fish: "RandomFishInterface"
) -> "PerfInfo":
    fish_iter = RandomFishIterator(fish, len=n)
    timer = PerfTimer()
    with timer:
        # list([i async for i in fish_iter])
        async for i in fish_iter:
            ...  # noqa: E704

    if __debug__:
        logging.debug(
            "random generator. %r. iterations: %r. %r.", fish, n, timer
        )
    return timer.get_info()


async def measure_random_list(
    n: int, fish: "RandomFishInterface"
) -> "PerfInfo":
    fish_list = RandomList(len=n, item=fish)
    timer = PerfTimer()
    with timer:
        await anext(fish_list)

    if __debug__:
        logging.debug("random list. %r. iterations: %r. %r.", fish, n, timer)
    return timer.get_info()


ITERATORS_INFO: list[
    t.Callable[[int, "RandomFishInterface"], t.Awaitable["PerfInfo"]]
] = [
    measure_range_next,
    measure_random_iterator,
    measure_random_list,
]


async def random_bool_fish_perf_test():
    logging.warning("%s:", random_bool_fish_perf_test.__name__)
    fish = RandomBool()

    for n in (1_000, 10_000, 100_000, 1_000_000):
        for _runner in ITERATORS_INFO:
            info = await _runner(n, fish)
            logging.info(
                f" {_runner.__name__} {n} iterations takes {info.nano} ns, "
                f"{info.micro} mks, {info.milli} ms, {info.seconds} s."
            )
        logging.info("-" * 12)


async def random_int_fish_perf_test():
    logging.warning("%s:", random_int_fish_perf_test.__name__)
    fish = RandomInt(1, 1_000_000_000)

    for n in (1_000, 10_000, 100_000, 1_000_000):
        for _runner in ITERATORS_INFO:
            info = await _runner(n, fish)
            logging.info(
                f" {_runner.__name__} {n} iterations takes {info.nano} ns, "
                f"{info.micro} mks, {info.milli} ms, {info.seconds} s."
            )
        logging.info("-" * 12)


async def random_float_fish_perf_test():
    logging.warning("%s:", random_float_fish_perf_test.__name__)
    fish = RandomFloat(0.0, 1.0)

    for n in (1_000, 10_000, 100_000, 1_000_000):
        for _runner in ITERATORS_INFO:
            info = await _runner(n, fish)
            logging.info(
                f" {_runner.__name__} {n} iterations takes {info.nano} ns, "
                f"{info.micro} mks, {info.milli} ms, {info.seconds} s."
            )
        logging.info("-" * 12)


async def random_tuple_fish_perf_test():
    logging.warning("%s:", random_tuple_fish_perf_test.__name__)
    fish = RandomTuple[tuple[int, float]](
        RandomInt(1, 1_000_000_000),
        RandomFloat(0.0, 1.0),
    )

    for n in (1_000, 10_000, 100_000, 1_000_000):
        for _runner in ITERATORS_INFO:
            info = await _runner(n, fish)
            logging.info(
                f" {_runner.__name__} {n} iterations takes {info.nano} ns, "
                f"{info.micro} mks, {info.milli} ms, {info.seconds} s."
            )
        logging.info("-" * 12)


async def main():
    await random_bool_fish_perf_test()
    await random_int_fish_perf_test()
    await random_float_fish_perf_test()
    await random_tuple_fish_perf_test()


if __name__ == "__main__":
    asyncio.run(main())
