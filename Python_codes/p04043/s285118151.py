import sys

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


def main():
    X = list(map(int, readline().split()))

    X.sort()
    if X[0] == 5 and X[1] == 5 and X[2] == 7:
        print('YES')
    else:
        print('NO')

    return


if __name__ == '__main__':
    main()
