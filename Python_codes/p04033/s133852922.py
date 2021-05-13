import sys
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
read = sys.stdin.buffer.read
sys.setrecursionlimit(10 ** 7)
INF = float('inf')

a, b = map(int, input().split())


if a * b < 0:
    print("Zero")
elif a == 0 or b == 0:
    print("Zero")
elif a > 0 and b > 0:
    print('Positive')
else:
    minus = abs(b - a) + 1
    if minus % 2 == 0:
        print('Positive')
    else:
        print('Negative')

