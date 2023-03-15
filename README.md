# Fancy Pythonic String Builder

[![image](https://img.shields.io/pypi/v/str_builder.svg)](https://pypi.python.org/pypi/str_builder)

[![image](https://img.shields.io/travis/sfermigier/str_builder.svg)](https://travis-ci.com/sfermigier/str_builder)

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

from str_builder import Builder

b = Builder("A")
b << "B"
with b(surround=("{ ", " }"), separator="; ") as b1:
    b1 << ["a", "b", "c"]

assert b.build() == "A B { a; b; c }"
```
