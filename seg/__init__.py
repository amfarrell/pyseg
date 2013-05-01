#!/usr/bin/env python

"""Python wrapper for the Stanford Word Segmenter.
@author Andrew M. Farrell
@date May 2013"""


from .client import (
    SocketSeg,
    HttpSeg,
)

from .exceptions import (
    NERError,
)


__version__ = '0.1'
VERSION = tuple(map(int, __version__.split('.')))

__all__ = [
    'SocketSeg',
    'HttpSeg',
    'SegError',
]
