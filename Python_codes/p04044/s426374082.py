#!/usr/bin/env python3


def main():
    N, L = map(int, input().split())
    S = [input() for _ in range(N)]
    print("".join(sorted(S)))


main()
