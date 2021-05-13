N = int(input())
L = list(map(int,input().split()))
L.sort()
ans = 0
i = 0
while(i<2*N):
  ans += L[i]
  i += 2
print(ans)