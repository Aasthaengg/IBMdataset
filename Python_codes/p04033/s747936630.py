# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

a, b = map(int, input().split())

if a > 0 and b > 0:
    print("Positive")
elif a * b <= 0:
    print("Zero")
elif (b - a) % 2 == 1:
    print("Positive")
else:
    print("Negative")
