# flake8: noqa: E402

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


def measure_range_next(n: int, fish: "RandomFishInterface") -> "PerfInfo":
    timer = PerfTimer()
    with timer:
        # list([next(fish) for _i in range(n)])
        for _i in range(n):
            next(fish)

    if __debug__:
        logging.debug("iter. %r. iterations: %r. %r.", fish, n, timer)
    return timer.get_info()


def measure_random_iterator(n: int, fish: "RandomFishInterface") -> "PerfInfo":
    fish_iter = RandomFishIterator(fish, len=n)
    timer = PerfTimer()
    with timer:
        # list(fish_iter)
        for i in fish_iter:
            ...  # noqa: E704

    if __debug__:
        logging.debug(
            "random generator. %r. iterations: %r. %r.", fish, n, timer
        )
    return timer.get_info()


def measure_random_list(n: int, fish: "RandomFishInterface") -> "PerfInfo":
    fish_list = RandomList(len=n, item=fish)
    timer = PerfTimer()
    with timer:
        next(fish_list)

    if __debug__:
        logging.debug("random list. %r. iterations: %r. %r.", fish, n, timer)
    return timer.get_info()


ITERATORS_INFO: list[t.Callable[[int, "RandomFishInterface"], "PerfInfo"]] = [
    measure_range_next,
    measure_random_iterator,
    measure_random_list,
]


def random_bool_fish_perf_test():
    logging.warning("%s:", random_bool_fish_perf_test.__name__)
    fish = RandomBool()

    for n in (1_000, 10_000, 100_000, 1_000_000):
        for _runner in ITERATORS_INFO:
            info = _runner(n, fish)
            logging.info(
                f" {_runner.__name__} {n} iterations takes {info.nano} ns, "
                f"{info.micro} mks, {info.milli} ms, {info.seconds} s."
            )
        logging.info("-" * 12)


def random_int_fish_perf_test():
    logging.warning("%s:", random_int_fish_perf_test.__name__)
    fish = RandomInt(1, 1_000_000_000)

    for n in (1_000, 10_000, 100_000, 1_000_000):
        for _runner in ITERATORS_INFO:
            info = _runner(n, fish)
            logging.info(
                f" {_runner.__name__} {n} iterations takes {info.nano} ns, "
                f"{info.micro} mks, {info.milli} ms, {info.seconds} s."
            )
        logging.info("-" * 12)


def random_float_fish_perf_test():
    logging.warning("%s:", random_float_fish_perf_test.__name__)
    fish = RandomFloat(0.0, 1.0)

    for n in (1_000, 10_000, 100_000, 1_000_000):
        for _runner in ITERATORS_INFO:
            info = _runner(n, fish)
            logging.info(
                f" {_runner.__name__} {n} iterations takes {info.nano} ns, "
                f"{info.micro} mks, {info.milli} ms, {info.seconds} s."
            )
        logging.info("-" * 12)


def random_tuple_fish_perf_test():
    logging.warning("%s:", random_tuple_fish_perf_test.__name__)
    fish = RandomTuple[tuple[int, float]](
        RandomInt(1, 1_000_000_000),
        RandomFloat(0.0, 1.0),
    )

    for n in (1_000, 10_000, 100_000, 1_000_000):
        for _runner in ITERATORS_INFO:
            info = _runner(n, fish)
            logging.info(
                f" {_runner.__name__} {n} iterations takes {info.nano} ns, "
                f"{info.micro} mks, {info.milli} ms, {info.seconds} s."
            )
        logging.info("-" * 12)


def main():
    random_bool_fish_perf_test()
    random_int_fish_perf_test()
    random_float_fish_perf_test()
    random_tuple_fish_perf_test()


if __name__ == "__main__":
    main()
