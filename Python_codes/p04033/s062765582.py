import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    a, b = map(int, readline().split())

    if a <= 0 <= b:
        print("Zero")
    else:
        if 0 < a:
            print("Positive")
        elif (-a + b + 1) % 2 == 0:
            print("Positive")
        else:
            print("Negative")


if __name__ == '__main__':
    main()
