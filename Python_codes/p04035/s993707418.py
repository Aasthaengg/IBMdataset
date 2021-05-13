import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    n, l = map(int, readline().split())
    a = list(map(int, readline().split()))
    b = [a[i] + a[i + 1] for i in range(n - 1)]

    last = -1
    for i, x in enumerate(b, 1):
        if x >= l:
            last = i
            break

    if last == -1:
        print("Impossible")
    else:
        print("Possible")
        for i in range(1, last):
            print(i)
        for i in range(n - 1, last, -1):
            print(i)
        print(last)


if __name__ == '__main__':
    main()
