from functools import singledispatch
import html
from typing import Any

# singledispatch marks the function that will handle the base type


@singledispatch
def htmlize(obj: Any):
    content = html.escape(repr(obj))
    return '<pre>{}</pre>'.format(content)
