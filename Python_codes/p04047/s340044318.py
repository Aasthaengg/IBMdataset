#!/usr/bin/env python3
import sys
sys.setrecursionlimit(10000000)
INF = 1<<32


def solve(N: int, L: "List[int]"):
    L.sort()
    print(sum([L[i] for i in range(2*N) if i%2 == 0]))
    return



def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    L = [int(next(tokens)) for _ in range(2 * N)]  # type: "List[int]"
    solve(N, L)

if __name__ == '__main__':
    main()
