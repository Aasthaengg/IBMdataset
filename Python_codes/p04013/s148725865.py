N, A = map(int, input().split())
X = list(map(int, input().split()))
for i in range(N):
  X[i] -= A
D = {0: 1}
for i in X:
  S = [[j, D[j]] for j in D]
  for j in S:
    if j[0] + i in D:
      D[j[0]+i] += j[1]
    else:
      D[j[0]+i] = j[1]
print(D[0]-1)