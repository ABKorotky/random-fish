# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project overview

`random-fish` is a Python 3.13 library that generates random values/objects via composable generator
classes ("fish"). Each generator supports both sync (`next()`) and async (`anext()`) protocols.

## Environment setup

```bash
python3.13 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -r requirements-dev.txt
```

## Common commands

All tooling is run via `tox` (see `tox.ini`, covering `random_fish`, `tests`, and `examples`).

- `tox` — runs the default envlist: `cs`, `ann`, `utc` (must pass before merging, per README).
- `tox -e format` — auto-formats code with `isort` then `black`. Run before committing.
- `tox -e cs` — code style check (`isort --check-only`, `black --check`, `flake8`).
- `tox -e ann` — type-check with `mypy`.
- `tox -e utc` — run unit tests under `coverage` (text + HTML report); fails if coverage < 95%
  (see `[tool.coverage.report] fail_under` in `pyproject.toml`).
- `tox -e doc` — regenerates `docs/modules` via `sphinx-apidoc` and builds HTML docs with `sphinx-build`.
- `tox -e build` — builds a sdist for distribution.
- `tox -e upload` — uploads a built dist to PyPI (`PYPI_REPOSITORY_ALIAS` env var selects
  `testpypi`/`pypi`, defaults to `testpypi`).

Running tests directly (without coverage), e.g. for a single file or case, use `unittest`:

```bash
python -m unittest tests.test_scalar
python -m unittest tests.test_scalar.RandomIntTestCase
python -m unittest tests.test_scalar.RandomIntTestCase.test_next
python -m unittest discover tests
```

## Architecture

### Core abstractions (`random_fish/base.py`)

Two generic interfaces everything builds on:

- `RandomFishInterface[T]` — a single-value generator. Implements `__next__() -> T` and
  `async __anext__() -> T`. Both must be implemented in tandem on every concrete class (the async
  version is usually a thin wrapper calling the sync `__next__`, except where it composes other
  async fish — see `structural.py`, `strings.py`).
- `RandomSchoolOfFishInterface[T]` — a generator of many values. Implements `__iter__()` and
  `__aiter__()`.

Concrete "fish" classes live in per-domain modules and are all re-exported from
`random_fish/__init__.py` (keep `__all__` there and the module-level `__all__` in sync when adding
new public classes):

- `scalar.py` — `RandomBool`, `RandomInt`, `RandomFloat`.
- `choice.py` — `RandomChoice` (pick from `*choices`), `RandomEnumChoice` (pick from an `Enum`).
  Both share `BaseRandomChoice`.
- `datetime.py` — `RandomDateTime`, implemented on top of `RandomInt` over a Unix timestamp range.
- `strings.py` — `RandomString` (chars from an alphabet), `RandomWord` (subclass using
  `ascii_letters`), `RandomTemplatedString` (fills a `str.format` template from other fish),
  `RandomText` (joins repeated `RandomFishInterface[str]` values, e.g. words, with spaces).
- `structural.py` — `RandomTuple` (positional fish -> tuple), `RandomDict`/`BaseRandomStructure`
  (named fish -> dict), `RandomDataclass` (named fish -> constructs a given dataclass type).
- `collections.py` — `RandomList`, `RandomSet` (both via `BaseRandomSequence`), `RandomMap`
  (key/value fish pairs, built internally from `RandomTuple` + `RandomFishIterator`).
- `iterators.py` — `RandomFishIterator`, the engine powering all length-based repetition. Takes an
  `item: RandomFishInterface[T]` and a `len: LengthType` (`int | RandomFishInterface[int]`, so
  lengths can themselves be randomized), and yields `item` values `len` times via `__iter__`/`__aiter__`.

### Composability pattern

Fish are designed to nest arbitrarily: a `RandomList`'s `item` can be a `RandomDataclass`, whose
fields can themselves be `RandomList`/`RandomMap`/other fish, and any `len` parameter can be a
fixed `int` or another `RandomInt` fish for randomized lengths. See `examples/demo/sync.py` and
`examples/demo/async.py` for representative nested usage, and `examples/performance/` for
sync-vs-async benchmarking scripts.

### Conventions to follow when adding a new fish class

- Subclass `RandomFishInterface[T]` (single value) or compose `RandomFishIterator` /
  `RandomSchoolOfFishInterface[T]` (multi-value).
- Implement both `__next__`/`__anext__` (or `__iter__`/`__aiter__`).
- Log the produced value at debug level, guarded by `if __debug__:`, matching the existing pattern:
  `logger.debug("instance: %r. value: %r.", self, val)`.
- Add the class to the module's `__all__` and to `random_fish/__init__.py`'s import + `__all__`.
- Use `t.TypeVar`/`t.Generic` for parametrized element types, following the existing `*TypeVar`
  naming (e.g. `ItemTypeVar`, `ValueTypeVar`).

## Testing conventions

- Tests mirror `random_fish/*.py` 1:1 as `tests/test_*.py`.
- `tests/helpers.py` provides `ClassTestingHelper[T]` (an `IsolatedAsyncioTestCase` subclass) — set
  `tst_cls` on the test case, build instances via `self.build_tst_obj(*args, **kwargs)`, store as
  `self.tst_obj` in `setUp`.
- Each behavior is typically tested twice: once via `test_next` (`next(self.tst_obj)`) and once via
  `test_anext` (`await anext(self.tst_obj)`), asserting the same constraints on both.
- Coverage must stay >= 95% (`tests/*` itself is excluded from coverage, see `pyproject.toml`).

## Releasing

Versioning lives in `random_fish/__init__.py` (`VERSION` tuple) and must be updated alongside
`CHANGELOG.md` (Keep a Changelog format) before a release. The branching/release/tagging flow is
documented in detail in `README.md` under "Releasing new distributions flow" — follow it exactly
when asked to cut a release (squash + rebase feature branches, `--ff-only` merges, monotonic tags
on `main`, release branches for maintaining old versions, cherry-picks between them).