N = int(input())
L = list(map(int, input().split()))
L.sort()
S = 0
for i in range (1, 2*N+1, 2):
  S += L[i-1]
print(S)