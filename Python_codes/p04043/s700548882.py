import math
import collections
import fractions
import itertools
import functools
import operator

def solve():
    iroha = list(map(int, input().split()))
    if iroha.count(5)==2 and iroha.count(7)==1:
        print("YES")
    else:
        print("NO")
    return 0

if __name__ == "__main__":
    solve()