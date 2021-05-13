#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Counter, defaultdict


def main():
    N, A = map(int, input().split())
    X = [int(x) - A for x in input().split()]

    result = Counter([0])

    for x in X:
        dct = defaultdict(int)
        for k, v in result.items():
            dct[k + x] += v
        result += dct

    print(result[0] - 1)


if __name__ == "__main__":
    main()
