import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    s = input()
    edge = collections.deque()
    for i in s:
        if i == "0":
            edge.append("0")
        elif i == "1":
            edge.append("1")
        elif len(edge) > 0:
            edge.pop()
    print("".join(edge))
    return 0

if __name__ == "__main__":
    solve()
