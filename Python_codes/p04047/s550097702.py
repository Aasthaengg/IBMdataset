###template###
import sys
def input(): return sys.stdin.readline().rstrip()
def mi(): return map(int, input().split())
###template###

N = int(input())
Ks = sorted(list(mi()), reverse=True)

i = 0
ans = 0
while i < (2*N):
  ans += min(Ks[i],Ks[i+1])
  i += 2

print(ans)

