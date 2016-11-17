# arraytools - Array-related helper functions

[![circleci](https://circleci.com/gh/apassant/arraytools.png)](https://circleci.com/gh/apassant/arraytools)
[![codecov](https://codecov.io/gh/apassant/arraytools/branch/master/graph/badge.svg)](https://codecov.io/gh/apassant/arraytools)

Array-related helper functions, e.g. `arraytools.flatten([[1, 2 ,[3]], 4])` to flatten an array of (nested) arrays.

"Arrays" include `list`, `tuple` and `set`.

## Installation

```
python setup.py install
```

## Examples

### `flatten`

Flatten a array of (nested) arrays.
E.g. `[[1, 2 ,[3]], 'a']` -> `[1, 2, 3, 'a']`

```
>>> from arraytools import flatten
>>> flatten([[1, 2 ,[3]], 'a'])
[1, 2, 3, 'a']
```

### `flatten_integers`

Flatten an array of (nested) arrays of integers only.
Raise a `TypeError` exception if other types are included
E.g. `[[1, 2 ,[3]], 4]` -> `[1, 2, 3, 4]`

```
>>> from arraytools import flatten_integers
>>> flatten_integers([[1, 2 ,[3]], 4])
[1, 2, 3, 4]
```

While

```
>>> from arraytools import flatten_integers
>>> flatten_integers([[1, 2 ,[3]], 'a'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "arraytools/flattening.py", line 49, in flatten_integers
    return flatten(array_to_flatten, (int))
  File "arraytools/flattening.py", line 42, in flatten
    "allowed_types": allowed_types
TypeError: Array must contain (<type 'list'>, <type 'tuple'>, <type 'set'>) or <type 'int'>
```

## Unit tests

```
pip install -r requirements-dev.txt
nosetests --with-coverage --cover-package=arraytools
```
