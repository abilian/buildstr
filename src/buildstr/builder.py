from functools import cache
from typing import Any


class Builder:
    def __init__(self, *args, surround=None, separator=" ", name="base", parent=None):
        self._parent = parent
        self._stack = []
        self._items = list(args)
        self._surround = surround
        self._separator = separator
        self._name = name

    def __lshift__(self, other: Any):
        if self._stack:
            active_subbuilder = self._stack[-1]
            return active_subbuilder << other

        if isinstance(other, (list, tuple)):
            self._items.extend(other)
        else:
            self._items.append(other)

        return self

    __ilshift__ = __lshift__
    __iadd__ = __lshift__

    def __call__(self, *args, surround=None, separator=" ", name="sub"):
        root = self._get_root()
        parent = root._stack[-1] if root._stack else root
        sub_builder = Builder(
            *args, surround=surround, separator=separator, parent=parent, name=name
        )
        parent._items.append(sub_builder)
        root._stack.append(sub_builder)
        return sub_builder

    @cache
    def _get_root(self):
        if not self._parent:
            return self
        return self._parent._get_root()

    def __enter__(self):
        return self._get_root()

    def __exit__(self, _exc_type, _exc_val, _exc_tb):
        self._get_root()._stack.pop()

    def build(self):
        body = self._separator.join(str(item) for item in self._items)
        if self._surround is None:
            return body
        return self._surround[0] + body + self._surround[1]

    def __str__(self):
        return self.build()

    def __repr__(self):  # pragma: no cover
        return f"Builder({self._name}, items={self._items})"

    # Convenience methods ?
    def nl(self):
        return self << "\n"
