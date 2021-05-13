import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    N, *A = map(int, read().split())

    ans = INF
    for x in range(-100, 101):
        tmp = 0
        for a in A:
            tmp += (x - a) ** 2
        if ans > tmp:
            ans = tmp

    print(ans)
    return


if __name__ == '__main__':
    main()
