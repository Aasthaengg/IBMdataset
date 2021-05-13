import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    x = list(map(int, readline().split()))

    if x.count(5) == 2 and x.count(7) == 1:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
