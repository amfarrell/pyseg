# PySEG

The Python interface to the [Stanford Word Segmenter](https://github.com/afarrell/stanford-).

## Project Homepage

* [Stanford Word Segmenter](http://nlp.stanford.edu/software/segmenter.shtml)


## Installation

    $ python setup.py install

## Basic Usage

    >>> import seg
    >>> tagger = seg.HttpNER(host='localhost', port=8080)
    >>> tagger.segment("英格蘭足總盃\n")
    TODO: put result here.

## License

BSD License

## Author

PySEG is developed by maintained by Andrew M. Farrell.
It can be found here: http://github.com/amfarrell/pyseg
It is based on PyNER which is developed by maintained by Dat Hoang.
and can be found here: http://github.com/dat/pyner
