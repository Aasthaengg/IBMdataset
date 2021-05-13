ans = 10 ** 9
n = int(input())
A = list(map(int,input().split()))
for i in range(-100,101):
  X = 0
  for j in range(n):
    X += (A[j] - i) ** 2
  ans = min(ans,X)
print(ans)