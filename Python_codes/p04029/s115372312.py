#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys


def std_in():
    return sys.stdin.readline().strip()


def _main():
    N = int(std_in())
    r = range(1, N + 1)
    print(sum(r))


if __name__ == "__main__":
    _main()
