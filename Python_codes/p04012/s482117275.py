import sys
from collections import Counter

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    w = readline().strip()
    c = Counter(w)

    ok = True
    for v in c.values():
        if v % 2:
            ok = False
            break

    if ok:
        print('Yes')
    else:
        print('No')

    return


if __name__ == '__main__':
    main()
