import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    s = input()
    ok = [{"N", "S"}, {"E", "W"}, {"N", "S", "E", "W"}]
    if set(s) in ok:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()
