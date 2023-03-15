# Fancy Pythonic String Builder

[![image](https://img.shields.io/pypi/v/buildstr.svg)](https://pypi.python.org/pypi/buildstr)

[![image](https://img.shields.io/travis/sfermigier/buildstr.svg)](https://travis-ci.com/sfermigier/buildstr)

[![Documentation Status](https://readthedocs.org/projects/str-builder/badge/?version=latest)](https://str-builder.readthedocs.io/en/latest/?version=latest)

-   Free software: Apache Software License 2.0
<!-- -   Documentation: <https://str-builder.readthedocs.io>. -->

## Features

- Builds strings in a pythonic way.
- We're using the `with` statement to build substrings.
- Python code can be interleaved with the string building. 

Useful for generating code.

## Example

```python

from buildstr import Builder

b = Builder("A")
b << "B"
with b(surround=("{ ", " }"), separator="; ") as b1:
    b1 << ["a", "b", "c"]

assert b.build() == "A B { a; b; c }"
```
