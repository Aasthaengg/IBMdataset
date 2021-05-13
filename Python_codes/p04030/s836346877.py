#!/usr/bin/python
# -*- coding: UTF-8 -*-

import sys


def std_in():
    return sys.stdin.readline().strip()


def editor(s):
    d = ""
    for c in s:
        if c == "0":
            d += c
        elif c == "1":
            d += c
        elif c == "B":
            d = d[0:-1]
    return d


def _main():
    s = std_in()
    print(editor(s))


if __name__ == "__main__":
    _main()
