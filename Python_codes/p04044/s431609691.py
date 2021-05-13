N, L = map(int, input().split())
S = sorted(list(input() for _ in range(N)))
print(*S, sep='')