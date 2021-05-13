# n, m, l = map(int, input().split())

# list_n = list(map(int, input().split()))

# n = input()
# list = [input() for i in range(N)

# list = [[i for i in range(N)] for _ in range(M)]

import sys
input = sys.stdin.readline

N, L = map(int, input().split())
S = []
for i in range(N):
    S.append(input().rstrip('\n'))
S.sort()
print(''.join(S))
