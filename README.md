# math
[![Upload Python Package](https://github.com/Parsa2820/math/actions/workflows/python-publish.yml/badge.svg)](https://github.com/Parsa2820/math/actions/workflows/python-publish.yml)
[![PyPI](https://img.shields.io/pypi/v/math-command-line?label=PyPI)](https://pypi.org/project/math-command-line/)

I often find myself opening a python shell from the command line in order to do some quick math. Now I don't have to.

## Installation
```bash
$ pip install math-command-line
```

## Usage
```bash
$ math 1+1
2
```
```bash
$ math 2**6
64
```
Don't forget to use quotes for expression which contain bash special characters or spaces.
```bash
$ math "sin(1)**2 + cos(1)**2"
1.0
```
```bash
$ math "(19*3 + 18*3 + 17*2 + 14*1) / 9"
17.666666666666668
```
