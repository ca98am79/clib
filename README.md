# clib

clib is a command line interface for Interactive Brokers backed by [IbPy](https://github.com/blampe/IbPy)

## Installation

	  $ python setup.py install

The IB API connects through [Trader Workstation (TWS)](http://www.interactivebrokers.com/en/?f=tws) or the IB Gateway, so you will also need to download and install one of them.  It needs to be running and connected to use clib.

## Options
  
  - `--host` defaults to 'localhost'
  - `--port` defaults to 7496
  - `--client` client id defaults to 0
  - `--verbose` defaults to 0

## Usage

Buy 500 AAPL at market:

	clib buy 500 AAPL
	
Sell 500 AAPL at market:

	clib sell 500 AAPL

## LICENSE - "MIT License"

Copyright (c) 2013 Mike Carson, http://ca98am79.com/

Permission is hereby granted, free of charge, to any person
obtaining a copy of this software and associated documentation
files (the "Software"), to deal in the Software without
restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following
conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
OTHER DEALINGS IN THE SOFTWARE.
