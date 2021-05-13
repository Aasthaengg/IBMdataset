from collections import deque
def solve():
  ans = ['Possible']
  N, L = map(int, input().split())
  A = list(map(int, input().split()))
  for i in range(N-1):
    if A[i]+A[i+1]>=L:
      ind = i
      break
  else:
    return ['Impossible']
  for i in range(1,ind+1):
    ans.append(i)
  for i in range(N-1,ind+1,-1):
    ans.append(i)
  ans.append(ind+1)
  return ans
print(*solve(),sep='\n')