import sys

read = sys.stdin.read
readline = sys.stdin.buffer.readline
sys.setrecursionlimit(10 ** 8)
INF = float('inf')
MOD = 10 ** 9 + 7


def main():
    A = list(map(int, readline().split()))
    A.sort()
    if A == [5,5,7]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
