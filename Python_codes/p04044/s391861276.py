n, l = map(int, input().split())
S = [input() for _ in range(n)]
print(*sorted(S), sep='')