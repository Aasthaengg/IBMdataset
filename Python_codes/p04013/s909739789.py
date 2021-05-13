import sys

readline = sys.stdin.readline
MOD = 10 ** 9 + 7
INF = float('INF')
sys.setrecursionlimit(10 ** 5)


def main():
    from collections import Counter

    n, a = map(int, readline().split())
    x = list(map(int, readline().split()))

    ans = 0
    counter = Counter()

    counter[0] += 1
    for i in range(n):
        cur = a - x[i]
        counter_next = Counter()
        for key, val in counter.items():
            counter_next[key] += val
            counter_next[cur + key] += val
        counter = counter_next

    print(counter[0] - 1)


if __name__ == '__main__':
    main()
