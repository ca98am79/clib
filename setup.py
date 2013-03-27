#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""clib - Command Line Interactive Brokers

clib is a command-line interface built on top of IbPy, a third-party implementation 
of the API used for accessing the Interactive Brokers on-line trading system.  clib 
implements functionality that allows you to connect to IB, request stock ticker
data, submit orders for stocks and options, and more - from the command line.
"""
from distutils.core import setup


classifiers = """
Development Status :: 4 - Beta
Environment :: Console
Intended Audience :: End Users/Desktop
Intended Audience :: Developers
License :: OSI Approved :: MIT License
Natural Language :: English
Operating System :: OS Independent
Programming Language :: Python
Topic :: Office/Business :: Financial
Topic :: Office/Business :: Financial :: Investment
Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator
"""


doclines = __doc__.split('\n')


setup(
    name = 'clib',
    version = "0", # make value
    description = doclines[0],
    author = 'Mike Carson',
    author_email = 'ca98am79@gmail.com',
    url = 'https://github.com/ca98am79/clib',
    license = 'BSD License',
    packages = ['IbPy/ib', 'IbPy/ib/lib', 'IbPy/ib/ext', 'IbPy/ib/opt', 'IbPy/ib/sym'],
	scripts = ['clib'],
    classifiers = filter(None, classifiers.split('\n')),
    long_description = '\n'.join(doclines[2:]),
    platforms = ['any'],
    download_url = 'https://github.com/ca98am79/clib/archive/master.zip',
)
