# Habrpars
=====
[![Build Status](https://travis-ci.org/mitrofun/topverbs.svg?branch=master)](https://travis-ci.org/mitrofun/topverbs) [![Coverage Status](https://coveralls.io/repos/github/mitrofun/topverbs/badge.svg?branch=master)](https://coveralls.io/github/mitrofun/topverbs?branch=master)

Analyzer of the frequency of use of nouns in the headings of posts on [habr](https://habr.com/)

Installation
=====
    pip3 install git+https://github.com/mitrofun/habrapars

Usage
=====
In console print command *habrapars*:
```bash
habrpars -p 2 -t 3
================================================================================
Count pages have been parsed: 2
Total count weeks: 1
Top: 3
------------------------- week: 2018-07-30 - 2018-08-05 ------------------------
август: 2   **
обзор: 2    **
система: 2  **
================================================================================
main ran in 0.89s
```
Format of usage ```habrapars [-h] [-p int] [-s int] [-t int]```

```p``` - page count

```s``` - start page

```t``` - top count

Use habrapars --help to see more details.

Requirements
=====
- python 3.6+

Contributors
=====
- [mitri4](https://github.com/habrapars)

License
=====
habrapars is released under the MIT License. See the LICENSE file for more details.
