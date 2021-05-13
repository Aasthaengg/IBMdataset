N, L = [int(a) for a in input().split()]
S = []
for i in range(N):
  S.append(input())

S = sorted(S)

print(*S,sep="")