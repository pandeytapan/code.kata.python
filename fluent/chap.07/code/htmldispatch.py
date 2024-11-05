from functools import singledispatch
import html
from typing import Any
import numbers

# singledispatch marks the function that will handle the base type


@singledispatch
def htmlize(obj: Any):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)


@htmlize.register(str)
def _(text):
    content = html.escape(text).replace('\n', '<br>\n')
    return '<pre>{0}</pre>'.format(content)


@htmlize.register(numbers.Integral)
def _(n):
    return '<pre>{0} (0:{0:x})</pre>'.format(n)
