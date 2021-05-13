N, L = map(int, input().split())
S = [0] * N
for i in range(N):
  S[i] = str(input())
  
S = sorted(S)
for i in range(N):
  print(S[i], end = "")



