N, L = [int(i) for i in input().split()]
S = sorted([input() for _ in range(N)])

print(*S, sep="")
