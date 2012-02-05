#!/usr/bin/env python


# import std
import os
from os import path
import re
import sys
# import third party
try:
    from setuptools import setup, find_packages
except ImportError:
    try:
        from ez_setup import use_setuptools
    except ImportError:
        print "can't find ez_setup"
        print "try: wget http://peak.telecommunity.com/dist/ez_setup.py"
        sys.exit(1)
    use_setuptools()
    from setuptools import setup, find_packages

if sys.version_info < (2, 6):
    print "We don't support old Python releases!"
    print "Come on, upgrade at least to Python2.6 :)"
    sys.exit(1)

sys.path.append(path.join(path.dirname(__file__), 'src'))

__version__ = '0.1'
__author__  = 'AnonToolBox Crew'
__author_email__ = 'anontoolbox@yahoo.com'
__package_data__ = [
    'README.rst',
    'Changelog',
    'License',
    'Makefile',
    'buildout'
]


setup(
    name = 'anontoolbox',
    version = __version__,
    author = __author__,
    author_email = __author_email__,
    description = open('README.rst').read().split('\n')[0],
    long_description = open('README.rst').read(),
    url = 'http://anonnewsde.tumblr.com',
    platforms = ["Python >= 2.6"],
    license = 'Apache Software License',
    package_dir = {'': 'src'},
    packages = find_packages('src'),
    package_data = {'': __package_data__},
    include_package_data = True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points = {
        'console_scripts': [
            'twitter=twitter.cmdline:main',
            'twitterbot=twitter.ircbot:main',
            'twitter-log=twitter.logger:main',
            'twitter-stream-example=twitter.stream_example:main'
        ]
    },
    install_requires=[
          'setuptools',
          'twitter'
    ]
)

