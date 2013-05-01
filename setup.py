#!/usr/bin/env python


import os

from seg import __version__

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open(os.path.join(os.path.dirname(__file__), 'README.md')) as fp:
    description = fp.read()

specs = {
    'name' : 'seg',
    'version' : __version__,
    'description' : 'Python client for the Stanford Named Entity Recognizer',
    'long_description' : description,
    'url' : 'http://github.com/amfarrell/pyseg',
    'author' : 'Andrew M. Farrell',
    'keywords' : ['seg', 'stanford word segmenter', 'stanford chinese word segmenter'],
    'license' : 'BSD',
    'packages' : ['seg'],
    'test_suite' : 'tests.all_tests',
    'classifiers' : (
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ),
}

if __name__=='__main__':
    setup(**specs)

